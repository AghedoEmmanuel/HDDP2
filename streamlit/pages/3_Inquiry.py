import streamlit as st

st.set_page_config(
    page_title="Any question that need answering",
    page_icon="",
)

st.write("# This has been provided to understand what is required by for a better prediction")
st.sidebar.success("For extra information.")

st.markdown (
    """
    ### This is to understand the parameters given in the diabetes section
    - Pregnancies – indicating the number of pregnancies had by the patient.
    - Glucose – the glucose level of the patient at the time of this test.
    - Blood Pressure – the patients’ blood pressure (mmHg).
    - Skin Thickness – the thickness of the patient’s skin (triceps’ skin fold thickness in mm).
    - Insulin – the insulin level of the patients (U/ml).
    - BMI – the body mass index of the patient (weight in kg, height in m2).
    - Diabetes Pedigree Function – the diabetes pedigree function of the patient should be calculated. This is the degree to which a patient has the probability of getting diabetes due to their lineage having it. The formula used is ∑▒(0.1 ×n) , where n refers to the number of family members with diabetes. first-degree relatives such as parents, and siblings are given a value of 1 for n, but second-degree relatives such as grandparents,and cousins are given a value of 0.5 for n.
    - Age – indicates the age of the patient. (in years)

    ### This is to understand the parameters given in the heart disease section
    - age – indicating the age of the patient (in years).
    - sex – indicating the sex of the patient (1 = male; 0 = female).
    - cp – indicating the type of chest pain currently being felt by the patient (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic).
    - trestbps - resting blood pressure (in mm Hg on admission to the hospital)
    - chol - serum cholesterol in mg/dl
    - fbs - (fasting blood sugar > 120 mg/dl) indicating the blood sugar level of patient after fasting for a required period (1 = true; 0 = false).
    - restecg - resting electrocardiographic results (Value 0: normal, Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria).
    - thalach - maximum heart rate achieved.
    - exang - Angina is chest pain or discomfort caused when your heart muscle doesn't get enough oxygen-rich blood. It may feel like pressure or squeezing in your chest (1 = yes; 0 = no).
    - old peak - ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot).
    - slope - the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping).
    - ca - number of major vessels colored by fluoroscopy.
    - thal – thallium stress test. Involves the evaluation of the blood flow to the heart (1 = normal; 2 = fixed defect; 3 = reversable defect).
    """
)