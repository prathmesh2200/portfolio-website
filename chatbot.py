# key = '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'

# from openai import OpenAI
# client = OpenAI()

# client.api_key

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo-0125",
#   messages=[],
#   temperature=1,
#   max_tokens=2048,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0,
#   response_format={
#     "type": "text"
#   }
# )

# print(response)

import openai
key = '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'
# Replace 'your-api-key' with your actual OpenAI API key
# openai.api_key = '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'
# openai.api_key = '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'
openai.api_key = key
def chat_with_openai(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
            messages=[
                {"role": "user", "content": prompt}
            ],
            # max_tokens=150,  # Limit response length
            n=1,  # Number of responses to return
            stop=None,  # You can define stop sequences here
            temperature=0.7  # Adjust the creativity of the response
        )
        
        # Extracting the content of the response
        reply = response.choices[0].message.content
        # reply = response['choices'][0]['message']['content']
        # print(response)#['choices'][0]['message']['content'])
        return reply
    
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    response = chat_with_openai(user_input)
    print(f"Chatbot: {response}")