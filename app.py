import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

st.title("Healthy Lifestyle Assistant")

age = st.text_input("Enter your age")
weight = st.text_input("Enter your weight")
goal = st.text_input("Your goal (weight loss / energy / fitness)")

if st.button("Generate Health Plan"):

    prompt = f"""
You are a helpful health and lifestyle assistant.
Give simple wellness tips.
Do not give medical diagnosis.

Age: {age}
Weight: {weight}
Goal: {goal}

Create:
1. Morning routine
2. Light exercise
3. Healthy eating tips
4. Hydration advice
5. Motivation
"""

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    st.write(response.text)
