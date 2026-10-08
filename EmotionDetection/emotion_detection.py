import requests

def emotion_detector(text_to_analyse):
    """Detect emotions in the supplied text using the Watson NLP API."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=payload, timeout=30)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response.raise_for_status()

    result = response.json()

    emotions = result["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness
    }

    dominant_emotion = max(
        emotion_scores,
        key=emotion_scores.get
    )

    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores
