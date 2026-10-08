"""Flask server for the Emotion Detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Detect emotions from the text supplied by the user."""

    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or not text_to_analyze.strip():
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    response = emotion_detector(text_to_analyze.strip())

    if response.get("dominant_emotion") is None:
        return jsonify({
            "error": "Invalid text! Please try again!"
        }), 400

    return jsonify(response)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
