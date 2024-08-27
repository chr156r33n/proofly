# app.py
import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Function to get feedback from OpenAI API
def get_feedback(text, purpose, pre_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": pre_prompt},
            {"role": "user", "content": f"Proofread the following text for the purpose of {purpose}: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app layout
st.title("Proofreading App")
text_input = st.text_area("Paste your work here:")
purpose_input = st.text_input("Purpose of the text:")
pre_prompt_input = st.text_area("Set a pre-prompt:")

if st.button("Get Feedback"):
    if text_input and purpose_input:
        feedback = get_feedback(text_input, purpose_input, pre_prompt_input)
        st.subheader("Feedback:")
        st.write(feedback)
    else:
        st.error("Please fill in all fields.")
