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

    # Generate health plan
    result = generator(prompt, max_length=250, do_sample=True, temperature=0.7)
    plan = result[0]['generated_text']

    # Show nicely in Streamlit
    st.subheader("Your Personalized Health Plan")
    st.write(plan)
