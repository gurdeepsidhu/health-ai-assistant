import streamlit as st
from transformers import pipeline

st.title("Healthy Lifestyle Assistant")

# User inputs
age = st.text_input("Enter your age")
weight = st.text_input("Enter your weight")
goal = st.text_input("Your goal (weight loss / energy / fitness)")

# Load a small Hugging Face model suitable for Streamlit free plan
generator = pipeline('text2text-generation', model='google/flan-t5-small', device=-1)

if st.button("Generate Health Plan"):
    prompt = f"""
You are a helpful health and lifestyle assistant.
Give general wellness advice only.
Do NOT give medical diagnosis or suggest medicines.

User information:
Age: {age}
Weight: {weight}
Goal: {goal}

Create:
1. Morning routine
2. Light exercise plan
3. Healthy eating tips
4. Hydration advice
5. Motivational message
"""

    result = generator(prompt, max_length=250)
    st.write(result[0]['generated_text'])
