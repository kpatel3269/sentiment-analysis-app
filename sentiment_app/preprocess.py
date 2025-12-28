from __future__ import annotations

from typing import List


def split_lines(text: str) -> List[str]:
    """Split user input into non-empty lines, preserving order."""
    if text is None:
        return []
    lines = [ln.strip() for ln in text.splitlines()]
    return [ln for ln in lines if ln]
