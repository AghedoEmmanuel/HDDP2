import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# with st.sidebar:
#     selected = option_menu("HDDP",
#                            ["General information",
#                             "Disease Prediction",
#                             "Heart Disease Prediction",
#                             "Inquiry"],
#                            default_index=0)

#     if (selected == 'General Infromation'):
#         st.write('#General')

#     if (selected == 'Diabetes Prediction'):
#         st.write('#Diabetes')

#     if (selected == 'Heart disease Prediction'):
#         st.title('Heart')

#     if (selected == 'Inquiry'):
#         st.title('Inquiry')

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to HDDP! 👋")
st.sidebar.success("General Information.")
st.markdown (
    """
    Some information on the diseases being predicted on this website. 
    For more info head over to [Mayo clinic](https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444).
   ### 1.Diabetes
    - What is diabetes?
    Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood
    glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.
    - What health problems can people with diabetes develop?
    Over time, high blood glucose leads to problems such as:
    - heart disease
    - stroke
    - kidney disease
    - eye problems
    - dental disease
    - nerve damage
    - foot problems
    What symptoms should you watch out for?
    -Feeling more thirsty than usual
    - Urinating more often
    - Losing weight without trying
    - Presence of ketones in urine
    - Feeling tired and weak
    - Feeling irritable
    - Having blurry visions
    - Having slow-healing sores
    - Getting a lot of infections

    ### 2. Heart Disease
    -What is heart disease?
    Heart disease describes a range of conditions that affect your heart. Diseases under the heart disease
            umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems
            (arrhythmias); and heart defects you're born with (congenital heart defects), among others.
            The term "heart disease" is often used interchangeably with the term "cardiovascular disease."
            Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that
            can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect
            your heart's muscle, valves or rhythm, also are considered forms of heart disease.
            Many forms of heart disease can be prevented or treated with healthy lifestyle choices.

    - These are symptoms to watch out for
        
    - Chest pain, chest tightness, chest pressure and chest discomfort (angina)
    - Shortness of breath
    - Pain, numbness, weakness or coldness in your legs or arms if the blood vessels in those parts of your
                body are narrowed
    -Pain in the neck, jaw, throat, upper abdomen or back
    ### All information gotten from Mayo clinic
    """
)
