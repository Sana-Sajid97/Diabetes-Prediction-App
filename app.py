# app.py
import streamlit as st
import pickle

# Load the trained diabetes model
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("Diabetes Prediction App")

st.write("""
This app predicts whether a person is likely to have diabetes based on medical inputs.
""")

# Input fields
age = st.number_input("Enter your age", min_value=1, max_value=120, value=25)
glucose = st.number_input("Enter glucose level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Enter blood pressure", min_value=0, max_value=200, value=70)
bmi = st.number_input("Enter BMI", min_value=0.0, max_value=70.0, value=25.0)
insulin = st.number_input("Enter insulin level", min_value=0, max_value=900, value=80)

# Predict button
if st.button("Predict"):
    input_data = [[age, glucose, blood_pressure, bmi, insulin]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The model predicts that this person **may have diabetes**.")
    else:
        st.success("✅ The model predicts that this person is **not likely to have diabetes**.")
