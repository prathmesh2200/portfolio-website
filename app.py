
import json
import chatbot
import openai
from flask import Flask, render_template, request, jsonify
import sqlite3
from dotenv import load_dotenv
import os

def read_data_from_db(db_name):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Dictionary to store both tables' data
    data = {}

    # Function to convert experience table data to dictionary
    def get_experience_data():
        cursor.execute("SELECT * FROM experience")
        experience_rows = cursor.fetchall()
        experience_dict = {}
        for i, row in enumerate(experience_rows):
            experience_dict[i] = {
                "id": row[0],
                "position": row[1],
                "company": row[2],
                "timeline": row[3],
                "description": row[4] if len(row) > 4 else None  # Check if description exists
            }
        return experience_dict

    # Function to convert education table data to dictionary
    def get_education_data():
        cursor.execute("SELECT * FROM education")
        education_rows = cursor.fetchall()
        education_dict = {}
        for i, row in enumerate(education_rows):
            education_dict[i] = {
                "id": row[0],
                "degree": row[1],
                "school": row[2],
                "timeline": row[3]
            }
        return education_dict

    # Store data from both tables in the data dictionary
    data['experience'] = get_experience_data()
    data['education'] = get_education_data()

    # Close the connection
    conn.close()

    return data

# Read data from json file
with open("data/index.json", encoding="UTF-8") as JSONDATA:
    DICTDATA = json.load(JSONDATA)

# Read data from SQLite
db_data = read_data_from_db('data/portfolio.db')
DICTDATA['body']['section']['education'] = db_data['education']
DICTDATA['body']['section']['experience'] = db_data['experience']
print(f"\njson data:{DICTDATA}\n")

# Load the content of your page (assuming it's static text)
with open("data/portfolio.txt", "r") as file:
    page_content = file.read()


# Load environment variables from .env file
load_dotenv('secrets.env')
# Access the API key
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)
# Set OpenAI API key
openai.api_key = api_key 


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

@app.route('/chat', methods=['POST'])
def chat_with_openai():
    data = request.json
    user_message = data['message']
    
    try:
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
        reply = response.choices[0].message.content
        return jsonify(reply=reply)

    except Exception as e:
        return jsonify(reply=f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
