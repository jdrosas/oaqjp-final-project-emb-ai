from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the emotion detection interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_endpoint():
    """Process text and return detected emotions."""
    text_to_analyse = request.args.get("text", "")

    if not text_to_analyse.strip():
        return jsonify({
            "error": "Invalid input. Please provide text to analyse."
        }), 400

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return jsonify({
            "error": "Unable to detect emotion."
        }), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
