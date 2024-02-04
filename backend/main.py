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
    video_id = data['video_id']
    insert_data(title, description, video_id)
    
    sentiment_score = []
    sentiment_score.append(analyze_sentiment(title))
    sentiment_score.append(analyze_sentiment(description))
    return jsonify(sentiment_score)
