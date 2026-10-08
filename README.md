# Emotion Detection Application

## Project Name

**Emotion Detection Application using Watson NLP**

## Description

This project is a web-based emotion detection application developed using the Watson NLP library and Flask.

The application analyzes a text input and identifies the following emotions:

* Anger
* Disgust
* Fear
* Joy
* Sadness

It also determines the dominant emotion expressed in the provided text.

## Technologies Used

* Python
* Watson NLP
* Flask
* Unittest
* Pylint

## Project Structure

```text
emotion-detection/
│
├── README.md
├── emotion_detection.py
├── test_emotion_detection.py
├── server.py
└── EmotionDetection/
    ├── __init__.py
    └── emotion_detection.py
```

## Application

The `emotion_detector()` function receives a text string and returns the emotion scores and the dominant emotion detected by Watson NLP.

The Flask application exposes the emotion detection functionality through a web interface.

## Testing

Unit tests are included in `test_emotion_detection.py` to validate the emotion detection functionality.

Static code analysis is performed using Pylint.

## Author

Emotion Detection Final Project
