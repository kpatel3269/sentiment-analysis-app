# Sentiment Analysis App (Flask)

A clean, recruiter-friendly **sentiment analysis web app** that scores each line of text as **Positive / Negative / Neutral**.

✅ Lightweight default backend (VADER)  
✅ Optional higher-accuracy backend (Transformers)  
✅ Tests + GitHub Actions CI  

---

## Features

- Analyze **single text** or **multiple lines** (each line is analyzed separately)
- Displays results in a clean table with a simple confidence score
- Uses a safe default backend that **doesn't require heavy ML downloads**
- Optional Transformers backend for higher accuracy (downloads model on first run)

---

## Tech Stack

- **Python**
- **Flask** (web server)
- **VADER Sentiment** (default model)
- Optional: **Hugging Face Transformers** + **PyTorch**
- **Pytest** + **GitHub Actions** (CI)

---

## Run locally

### 1) Setup

```bash
python -m venv venv
source venv/bin/activate   # mac/linux
# venv\Scripts\activate  # windows

pip install -r requirements.txt
```

### 2) Start the app

```bash
python run.py
```

Open: `http://localhost:5000`

---

## Optional: use Transformers backend (higher accuracy)

```bash
pip install -r requirements-transformers.txt
export SENTIMENT_BACKEND=transformers   # mac/linux
# set SENTIMENT_BACKEND=transformers    # windows (cmd)
python run.py
```

You can also set a specific HF model:

```bash
export HF_SENTIMENT_MODEL=distilbert-base-uncased-finetuned-sst-2-english
```

---

## Project structure

```
sentiment-analysis-app/
  sentiment_app/
    factory.py
    routes.py
    sentiment.py
    preprocess.py
  templates/
    index.html
  static/
    styles.css
  tests/
    test_preprocess.py
    test_sentiment_vader.py
  run.py
  requirements.txt
  requirements-transformers.txt
```

---

## Roadmap

- Add CSV upload for batch scoring
- Add Dockerfile for one-command deploy
- Add model evaluation notebook (accuracy/F1) and model card

---

## License

MIT
