from flask import Flask, request, jsonify
from sentimental_analysis import analyze_sentiment
from sqlstore import insert_data
import os
import json


app = Flask(__name__)


@app.route('/video', methods=['POST']):
def video() -> str:
    """
    Get the video data and insert it into the database.

    """
    data = request.get_json()
    title = data['title']
    description = data['description']
    video_id = data['video_id'] # store the video id as a primary key in the database
    insert_data(title, description, video_id)
    
    sentiment_score = []
    sentiment_score.append(analyze_sentiment(title)) #check if the title is positive or negative
    sentiment_score.append(analyze_sentiment(description)) #check if the description is positive or negative
    return jsonify(sentiment_score) 


app.run(debug=True, port=5000)