from __future__ import annotations

from flask import Blueprint, render_template, request

from .sentiment import SentimentService

bp = Blueprint("main", __name__)
service = SentimentService()


@bp.route("/", methods=["GET", "POST"])
def index():
    results = None
    error = None
    backend = service.backend

    if request.method == "POST":
        text = (request.form.get("text") or "").strip()
        if not text:
            error = "Please enter some text."
        else:
            try:
                results = service.analyze(text)
                if not results:
                    error = "No valid lines to analyze. Try typing a sentence."
            except Exception as e:
                error = f"Something went wrong while analyzing sentiment: {e}"

    return render_template("index.html", results=results, error=error, backend=backend)
