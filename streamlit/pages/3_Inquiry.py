import streamlit as st

st.set_page_config(
    page_title="Any question that need answering",
    page_icon="",
)

st.write("# This has been provided to understand what is required by for a better prediction")
st.sidebar.success("For extra information.")

st.markdown(
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
    - chest pain type – indicating the type of chest pain currently being felt by the patient (Value 0: typical angina, Value 1: atypical angina, Value 2: non-anginal pain, Value 3: asymptomatic).
    - resting blood pressure - resting blood pressure (in mm Hg on admission to the hospital). You are making of the diastolic blood pressure.
    - cholestoral - serum cholesterol in mg/dl
    - fasting blood sugar - (fasting blood sugar > 120 mg/dl) indicating the blood sugar level of patient after fasting for a required period (1 = true; 0 = false).
    - Resting electrocardiographic - resting electrocardiographic results (Value 0: normal, Value 1: having ST-T wave abnormality (mild symptoms to severe problems signals non- normal heart beat), Value 2: Possible or definite left ventricular hypertrophy Enlarged heart's main pumping chamber (severe condition)).
    - Maximum heart rate - The highest number of beats per minute achieved by the patient's heart during a physical stress.
    - exercise induced angina - Angina is chest pain or discomfort caused when your heart muscle doesn't get enough oxygen-rich blood. It may feel like pressure or squeezing in your chest (1 = yes; 0 = no).
    - old peak - ST depression induced by exercise relative to rest looks at stress of heart during exercise unhealthy heart will stress more ('ST' relates to positions on the ECG plot).
    - slope - the slope of the peak exercise ST segment ( Value 0: upsloping (it shows better heart rate with exercise (uncommon)),
                Value 1: flat (it shows the minimal change (typical healthy heart)), 
                Value 2: downsloping(it shows the signs of unhealthy heart)).
    - vessels colored by flourosopy - number of major vessels (0-4) colored by flourosopy (Fluorescent colour is mainly associated with diabetes)
    - thallium stress test – The results of this test will tell you about the flow of blood to your heart through your coronary arteries    . 
            1 = normal; 2= fixed defect (used to be defect but ok now); 3 = reversable defect (no proper blood movement when exercising)
    """
)
