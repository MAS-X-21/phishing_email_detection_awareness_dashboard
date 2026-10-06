from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "phishing_text_model.joblib"

def load_model():
    if not MODEL_PATH.exists():
        return None
    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None

def predict(text):
    model = load_model()
    if model is None:
        return None, None
    probabilities = model.predict_proba([text])[0]
    classes = list(model.classes_)
    phishing_index = classes.index(1) if 1 in classes else 0
    return float(probabilities[phishing_index]), int(model.predict([text])[0])
