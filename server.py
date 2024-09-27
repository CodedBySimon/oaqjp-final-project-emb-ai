from flask import Flask, render_template, request
from Emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    dominant_emotion = response.popitem()


    # Return a formatted string with the sentiment label and score
    return "For the given statement  {}. The dominant emotion is {}.".format(response, dominant_emotion)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000)