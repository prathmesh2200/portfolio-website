
import json
import chatbot
from flask import Flask, render_template, request, jsonify


with open("portfolio-website/data/index.json", encoding="UTF-8") as JSONDATA:
    DICTDATA = json.load(JSONDATA)


app = Flask(__name__, template_folder="template")


@app.route("/")
def index() -> str:
    """Definition to render root HTML page"""
    return render_template('index.html', **DICTDATA)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    bot_response = chatbot.get_response(user_message)  # Chatbot logic
    return jsonify({'response': bot_response})

@app.route("/bio_instagram")
def instgram_bio_page() -> str:
    """Definition to render Instagram Bio HTML page"""
    return render_template("instagram_bio.html", **DICTDATA)
