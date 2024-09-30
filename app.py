
import json

from flask import Flask, render_template


with open("portfolio-website/data/index.json", encoding="UTF-8") as JSONDATA:
    DICTDATA = json.load(JSONDATA)


app = Flask(__name__, template_folder="template")


@app.route("/")
def index() -> str:
    """Definition to render root HTML page"""
    return render_template('index.html', **DICTDATA)


@app.route("/bio_instagram")
def instgram_bio_page() -> str:
    """Definition to render Instagram Bio HTML page"""
    return render_template("instagram_bio.html", **DICTDATA)
