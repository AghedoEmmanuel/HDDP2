import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.set_page_config(page_title="Diabetes Prediction", page_icon="📈")
st.markdown("# Diabetes Prediction")
st.sidebar.header("Diabetes Prediction")

Pregnancies = st.number_input("Number of Pregnancies")
Glucose = st.number_input("Glucose Level")
BloodPressure = st.number_input("Blood Pressure value")
SkinThickness = st.number_input("Skin Thickness value")
Insulin = st.number_input("Insulin level")
BMI = st.number_input("BMI")
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value")
Age = st.number_input("Age of patient")

diab_diagnosis = ''

if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diab_prediction[0] == 1):
        diab_diagnosis = "Patient has diabetes"
    else:
        diab_diagnosis = "Patient does not have diabetes"

st.success(diab_diagnosis)
