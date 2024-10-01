from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key
key = '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'
openai.api_key = key  # Replace with your OpenAI API key

# Load the content of your page (assuming it's static text)
with open("portfolio-website/data/portfolio.txt", "r") as file:
    page_content = file.read()

# Function to interact with OpenAI based on your page content
def chat_with_openai(prompt):
    try:
        # Concatenate the page content with the user prompt
        full_prompt = f"The following is the content of my portfolio:\n\n{page_content}\n\nUser question: {prompt}"

        # Send the prompt to OpenAI
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7  # Adjust temperature for creativity
        )
        
        # Extract the content of the response
        reply = response.choices[0].message.content
        return reply
    
    except Exception as e:
        return f"An error occurred: {e}"

# API route to handle POST requests for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json  # Get JSON data from the request
        prompt = data.get('prompt', '')  # Extract the prompt from the JSON payload
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        # Get the response from OpenAI
        response = chat_with_openai(prompt)
        
        return jsonify({"response": response}), 200  # Return the response as JSON
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5001)