# app.py
import streamlit as st
import openai

# Set your OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Function to get feedback from OpenAI API
def get_feedback(text, purpose, pre_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",  # Specify the model (or another completion model)
        prompt=f"{pre_prompt}\nProofread the following text for the purpose of {purpose}: {text}",
        max_tokens=150,  # Adjust max tokens as needed
        temperature=0.7  # Adjust temperature for creativity
    )
    return response['choices'][0]['text'].strip()  # Extract the text from the response

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
