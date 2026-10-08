import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestDominantEmotions(unittest.TestCase):
    """Test the dominant emotion returned by Watson NLP."""

    def get_emotion(self, text: str) -> str:
        """Return the dominant emotion for the supplied text."""
        emotions = emotion_detector(text)
        return emotions.get("dominant_emotion")

    def test_joy(self):
        """Test joy detection."""
        dominant_emotion = self.get_emotion(
            "I am glad this happened"
        )
        self.assertEqual(dominant_emotion, "joy")

    def test_anger(self):
        """Test anger detection."""
        dominant_emotion = self.get_emotion(
            "I am really mad about this"
        )
        self.assertEqual(dominant_emotion, "anger")

    def test_disgust(self):
        """Test disgust detection."""
        dominant_emotion = self.get_emotion(
            "I feel disgusted just hearing about this"
        )
        self.assertEqual(dominant_emotion, "disgust")

    def test_sadness(self):
        """Test sadness detection."""
        dominant_emotion = self.get_emotion(
            "I am so sad about this"
        )
        self.assertEqual(dominant_emotion, "sadness")

    def test_fear(self):
        """Test fear detection."""
        dominant_emotion = self.get_emotion(
            "I am really afraid that this will happen"
        )
        self.assertEqual(dominant_emotion, "fear")


if __name__ == "__main__":
    unittest.main()
