import streamlit as st
from transformers import pipeline

# Title
st.title("Healthy Lifestyle Assistant")

# User inputs
age = st.text_input("Enter your age")
weight = st.text_input("Enter your weight")
goal = st.text_input("Your goal (weight loss / energy / fitness)")

# Only load the model after user clicks button to save memory
if st.button("Generate Health Plan"):
    if not age or not weight or not goal:
        st.error("Please enter all fields!")
    else:
        # Load a small Hugging Face model suitable for free hosting
        generator = pipeline('text-generation', model='google/flan-t5-small', device=-1)

        # Create prompt
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

        # Generate health plan
        result = generator(prompt, max_length=250, do_sample=True, temperature=0.7)
        plan = result[0]['generated_text']

        # Display
        st.subheader("Your Personalized Health Plan")
        st.write(plan)
