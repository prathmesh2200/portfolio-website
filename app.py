
import json
import chatbot
import openai
from flask import Flask, render_template, request, jsonify


with open("portfolio-website/data/index.json", encoding="UTF-8") as JSONDATA:
    DICTDATA = json.load(JSONDATA)

# Load the content of your page (assuming it's static text)
with open("portfolio-website/data/portfolio.txt", "r") as file:
    page_content = file.read()

app = Flask(__name__, template_folder="template")
# Set OpenAI API key
key = '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'
openai.api_key = key 


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

@app.route('/chat', methods=['POST'])
def chat_with_openai():
    data = request.json
    user_message = data['message']
    
    try:
        # Define your page content here if necessary
        # page_content = "The following is the content of my portfolio."  # Replace with actual content
        # full_prompt = f"{page_content}\n\nUser question: {user_message}"
        # Concatenate the page content with the user prompt
        full_prompt = f"The following is the content of my portfolio:\n\n{page_content}\n\nUser question: {user_message}"

        # Call OpenAI API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7  # Adjust temperature for creativity
        )
        
        # Extract the response content
        # reply = response.choices[0].message['content']
        reply = response.choices[0].message.content
        return jsonify(reply=reply)

    except Exception as e:
        return jsonify(reply=f"An error occurred: {str(e)}")
