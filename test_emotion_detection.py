import unittest

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for the emotion detector."""

    def test_joy(self):
        result = emotion_detector(
            "I am so glad this is working."
        )
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        result = emotion_detector(
            "I am extremely angry about this situation."
        )
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = emotion_detector(
            "This is absolutely disgusting."
        )
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_fear(self):
        result = emotion_detector(
            "I am really afraid of what might happen."
        )
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_sadness(self):
        result = emotion_detector(
            "I feel very sad and disappointed."
        )
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
