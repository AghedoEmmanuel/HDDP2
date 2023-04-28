import pickle
import streamlit as st

hd_model = pickle.load(
    open('./saved_models/heart_disease_model.sav','rb'))

st.set_page_config(page_title="Heart Disease Prediction", page_icon="📈")
st.markdown("# Heart Disease Prediction")
st.sidebar.header("Heart Disease Prediction")

age = st.number_input("Age of Patient")
sex = st.number_input("Gender of the Patient")
cp = st.number_input("Indicate the type of chest pain on a range from 0-4")
trestbps = st.number_input("Patients resting blood pressure in mmHg")
chol = st.number_input("Serum choestoral")
fbs = st.number_input("Fasting blood sugar")
restecg = st.number_input(
    "Resting electrocardiographic results on a range from 0-2")
thalach = st.number_input("Maximum heart rate achieved")
exang = st.number_input("Exercise Induced Angina on a range from 0-1")
oldpeak = st.number_input("ST depression induced by exercise relative to rest")
slope = st.number_input("The slope of the peak exercise ST segment")
ca = st.number_input("Number of major vessels (0-3) colored by flourosopy")
thal = st.number_input("Thallium stress test range of 1-3")

hd_diagnosis = ''

if st.button('Heart Disease Test Result'):
    hd_prediction = hd_model.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if (hd_prediction[0] == 1):
        hd_diagnosis = "Patient has diabetes"
    else:
        hd_diagnosis = "Patient does not have diabetes"

st.success(hd_diagnosis)

st.markdown(
    """
    For more information visit the inquiry page
    """
)
