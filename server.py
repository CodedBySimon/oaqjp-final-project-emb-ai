"""
Emotion Detector Flask Application

This module creates a Flask web application for detecting emotions in text 
using an external emotion detection service.

Routes:
    /: Renders the index page.
    /emotionDetector: Analyzes the provided text for emotions and returns the dominant emotion.

Functions:
    render_index_page(): Renders the index.html template.
    detect_emotion(): Retrieves text from the request, analyzes it for emotions, 
    and returns the dominant emotion.

Usage:
    Run this script to start the Flask web server. 
    The server will be accessible at http://0.0.0.0:5000.

Example:
    To start the server, run:
        python server.py

Dependencies:
    Flask: A micro web framework for Python.
    Emotion_detection.emotion_detection: A module for detecting emotions in text.

"""
from flask import Flask, render_template, request
from Emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#show index php
@app.route("/")
def render_index_page():
    return render_template('index.html')

#handle input
@app.route("/emotionDetector")
def detect_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion']is None:
        return " Invalid text! Please try again!"

    # Extract the label and score from the response
    dominant_emotion = response.popitem()

    #Return a result
    return "For the given statement  {}. The dominant emotion is {}.".format(response, dominant_emotion)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
