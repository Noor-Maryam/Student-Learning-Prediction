from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

model_path = Path(__file__).with_name("student_pipeline.joblib")
st.set_page_config(page_title="Student Pass/Fail Demo")
st.title("Student Pass/Fail Demo")
st.caption("Classroom demo using synthetic data. Do not use it to judge or penalize students.")

if not model_path.is_file():
    st.error("Keep student_pipeline.joblib beside app.py, or run the notebook to create it.")
    st.stop()

@st.cache_resource
def load_pipeline():
    return joblib.load(model_path)

with st.form("student_details"):
    hours_studied = st.number_input("Hours studied", min_value=0.0, value=5.0, step=0.1)
    attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=80)
    practice_tests = st.number_input("Practice tests completed", min_value=0, value=3)
    sleep_hours = st.number_input("Hours of sleep", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
    study_method = st.selectbox("Study method", ["self", "group", "video"])
    submitted = st.form_submit_button("Predict")

if submitted:
    student = pd.DataFrame([{
        "hours_studied": hours_studied,
        "attendance": attendance,
        "practice_tests": practice_tests,
        "sleep_hours": sleep_hours,
        "study_method": study_method,
    }])
    prediction = load_pipeline().predict(student)[0]
    outcome = "Pass" if prediction == 1 else "Fail"
    st.info(f"Predicted outcome: {outcome}")
