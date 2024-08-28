# app.py
import streamlit as st
import requests
import json

# Function to call the OpenAI API directly
def call_openai_api(api_key, prompt, pre_prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",  # Specify the model
        "messages": [
            {"role": "system", "content": pre_prompt},  # Use the user-defined pre-prompt
            {"role": "user", "content": prompt}  # User message
        ],
        "max_tokens": 1500,
        "temperature": 0.1
    }
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    return response.json()  # Return the JSON response

# Streamlit app layout
st.title("Proofreading App")
text_input = st.text_area("Paste your work here:")
purpose_input = st.text_input("Purpose of the text:")
pre_prompt_input = st.text_area("Set a pre-prompt:")

if st.button("Get Feedback"):
    if text_input and purpose_input and pre_prompt_input:
        api_key = st.secrets["openai"]["api_key"]  # Get API key from Streamlit secrets
        prompt = f"Proofread the following text for the purpose of {purpose_input}: {text_input}"
        feedback_response = call_openai_api(api_key, prompt, pre_prompt_input)
        
        # Extract the content from the response
        if 'choices' in feedback_response and len(feedback_response['choices']) > 0:
            feedback = feedback_response['choices'][0]['message']['content']
            st.subheader("Feedback:")
            st.write(feedback)
        else:
            st.error("Error in response from OpenAI API.")
    else:
        st.error("Please fill in all fields.")
