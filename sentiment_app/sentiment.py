from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, List, Optional

from .preprocess import split_lines

# We support two backends:
# - 'vader' (default): lightweight, no downloads
# - 'transformers': higher accuracy, downloads a model on first run


@dataclass(frozen=True)
class SentimentResult:
    text: str
    label: str
    score: float  # 0..1 confidence-ish


def _normalize_label(label: str) -> str:
    label = (label or "").upper().strip()
    if label in {"POSITIVE", "POS"}:
        return "POSITIVE"
    if label in {"NEGATIVE", "NEG"}:
        return "NEGATIVE"
    if label in {"NEUTRAL", "NEU"}:
        return "NEUTRAL"
    return label or "UNKNOWN"


class SentimentService:
    def __init__(self, backend: Optional[str] = None):
        self.backend = (backend or os.getenv("SENTIMENT_BACKEND", "vader")).lower().strip()
        self._predictor = None

    def analyze(self, text: str) -> List[SentimentResult]:
        items = split_lines(text)
        if not items:
            return []
        predictor = self._get_predictor()
        raw = predictor(items)

        results: List[SentimentResult] = []
        for item, r in zip(items, raw):
            label = _normalize_label(r.get("label"))
            score = float(r.get("score", 0.0))
            results.append(SentimentResult(text=item, label=label, score=score))
        return results

    def _get_predictor(self):
        if self._predictor is not None:
            return self._predictor

        if self.backend == "transformers":
            try:
                from transformers import pipeline  # type: ignore
            except Exception as e:
                # Fallback gracefully
                self.backend = "vader"
            else:
                model_name = os.getenv(
                    "HF_SENTIMENT_MODEL",
                    "distilbert-base-uncased-finetuned-sst-2-english",
                )
                pipe = pipeline("sentiment-analysis", model=model_name)

                def _pred(items: List[str]) -> List[Dict[str, float]]:
                    out = pipe(items)
                    # transformers returns [{"label": "...", "score": ...}, ...]
                    return [{"label": o["label"], "score": float(o["score"])} for o in out]

                self._predictor = _pred
                return self._predictor

        # Default / fallback: VADER
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # type: ignore

        analyzer = SentimentIntensityAnalyzer()

        def _pred(items: List[str]) -> List[Dict[str, float]]:
            out: List[Dict[str, float]] = []
            for t in items:
                scores = analyzer.polarity_scores(t)
                compound = float(scores.get("compound", 0.0))
                # Map compound [-1,1] to a label + pseudo-confidence
                if compound >= 0.05:
                    label = "POSITIVE"
                elif compound <= -0.05:
                    label = "NEGATIVE"
                else:
                    label = "NEUTRAL"
                confidence = min(1.0, abs(compound))  # 0..1, simple proxy
                out.append({"label": label, "score": confidence})
            return out

        self._predictor = _pred
        return self._predictor
