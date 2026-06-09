import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("Diabetes Prediction App")
st.write("Enter the details to predict whether a person has diabetes.")

# Input fields
preg = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose Level", 0, 200, 120)
bp = st.number_input("Blood Pressure", 0, 122, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin Level", 0, 900, 79)
bmi = st.number_input("BMI", 0.0, 70.0, 20.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 0, 120, 33)

# Predict button
if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("The person **may have diabetes**.")
    else:
        st.success("The person **is unlikely to have diabetes**.")
