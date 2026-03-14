import streamlit as st

st.title("Healthy Lifestyle Assistant")

age = st.text_input("Enter your age")
weight = st.text_input("Enter your weight")
goal = st.text_input("Your goal (weight loss / energy / fitness)")

if st.button("Generate Health Plan"):
    if not age or not weight or not goal:
        st.error("Please enter all fields!")
    else:
        st.subheader("Your Personalized Health Plan")
        st.write("**Morning Routine:** Wake up at 6:30 AM, do light stretching for 10 mins")
        st.write("**Light Exercise:** 20-minute walk or yoga session")
        st.write("**
