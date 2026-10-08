# Emotion Detection Application using Watson NLP

## Project Description

This project is a web application that detects emotions in text using the Watson NLP Emotion Prediction service.

The application analyzes a given text and identifies the following emotions:

* Anger
* Disgust
* Fear
* Joy
* Sadness

It also determines the dominant emotion detected in the text.

## Technologies Used

* Python
* Flask
* Watson NLP
* Requests
* Unittest
* HTML/CSS
* Git and GitHub

## Project Structure

```text
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── static/
├── templates/
├── emotion_detection.py
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Features

* Emotion detection using Watson NLP.
* Detection of five emotions.
* Identification of the dominant emotion.
* Error handling for invalid or empty input.
* Flask web interface.
* Unit testing.
* Static code analysis using Pylint.

## How to Run

Start the Flask application with:

```bash
python3 server.py
```

Then open the application in a web browser through the configured Flask port.

## Testing

Run the unit tests with:

```bash
python3 test_emotion_detection.py
```

Static analysis can be performed with:

```bash
pylint server.py
```

## Project Name

**Emotion Detection Application using Watson NLP**
