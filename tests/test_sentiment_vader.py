from sentiment_app.sentiment import SentimentService


def test_vader_backend_returns_results():
    svc = SentimentService(backend="vader")
    out = svc.analyze("I love this.\nI hate this.")
    assert len(out) == 2
    assert out[0].text == "I love this."
    assert out[1].text == "I hate this."
    assert out[0].label in {"POSITIVE", "NEGATIVE", "NEUTRAL"}
    assert 0.0 <= out[0].score <= 1.0
