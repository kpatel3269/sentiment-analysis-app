from sentiment_app.preprocess import split_lines


def test_split_lines_strips_and_drops_empty():
    text = " hello\n\n world \n  \n"
    assert split_lines(text) == ["hello", "world"]


def test_split_lines_none():
    assert split_lines(None) == []
