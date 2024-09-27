from Emotion_detection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        #Test for joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        #Test for anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        
        #test for disgust
        result_3 = emotion_detector('I feel digusted just hearing about this, Mr. P.Diddy. Just so disgusted...')
        self.assertEqual(result_3['dominant_emotion'],'disgust')

        #Test for sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        #Test for fear
        result_5 = emotion_detector('I am really afraid this will happen again, Mr. P.Diddy')
        self.assertEqual(result_5['dominant_emotion'], 'fear')


unittest.main()