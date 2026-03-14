import streamlit as st

st.title("Healthy Lifestyle Assistant")

# User inputs
age = st.text_input("Enter your age")
weight = st.text_input("Enter your weight")
goal = st.text_input("Your goal (weight loss / energy / fitness)")

if st.button("Generate Health Plan"):
    if not age or not weight or not goal:
        st.error("Please enter all fields!")
    else:
        st.subheader("Your Personalized Health Plan")

        # Example health plan (safe for free Streamlit)
        st.write("**Morning Routine:** Wake up at 6:30 AM, do light stretching for 10–15 minutes, drink a glass of warm water with lemon.")
        st.write("**Light Exercise:** 20–30 minute walk, or gentle yoga session.")
        st.write("**Healthy Eating Tips:** Include fruits, vegetables, and lean protein; avoid fried and sugary foods.")
        st.write("**Hydration Advice:** Drink at least 8 glasses of water throughout the day.")
        st.write("**Motivational Message:** Remember, small consistent steps lead to big changes. You’ve got this! ✅")
