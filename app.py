import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("adhd_overload_regressor.pkl")

st.set_page_config(
    page_title="ADHD Overload Predictor",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 ADHD Cognitive Overload Predictor")
st.write(
    "Enter details about your day to estimate your **mental overload level**."
)

st.divider()

# -------- User Inputs --------
sleep_hours = st.slider(
    "🛌 Sleep Hours",
    min_value=0.0,
    max_value=10.0,
    value=6.0,
    step=0.5
)

screen_time_hours = st.slider(
    "📱 Screen Time (hours)",
    min_value=0.0,
    max_value=15.0,
    value=6.0,
    step=0.5
)

stress_level = st.slider(
    "😖 Stress Level (1–10)",
    min_value=1,
    max_value=10,
    value=5
)

task_count = st.slider(
    "📋 Number of Tasks",
    min_value=0,
    max_value=15,
    value=5
)

focus_score = st.slider(
    "🎯 Focus Score (1–10)",
    min_value=1,
    max_value=10,
    value=5
)

st.divider()

# -------- Prediction --------
if st.button("🔍 Predict Overload"):
    input_data = pd.DataFrame([[
        sleep_hours,
        screen_time_hours,
        stress_level,
        task_count,
        focus_score
    ]], columns=[
        "sleep_hours",
        "screen_time_hours",
        "stress_level",
        "task_count",
        "focus_score"
    ])

    overload_score = model.predict(input_data)[0]
    overload_score = np.clip(overload_score, 0, 100)

    st.subheader("📊 Results")
    st.metric("Overload Score", f"{overload_score:.1f} / 100")

    # Interpretation
    if overload_score < 35:
        level = "Low"
        advice = "You seem mentally comfortable today. Maintain this balance 🌱"
        color = "🟢"
    elif overload_score < 65:
        level = "Moderate"
        advice = "Some strain detected. Consider breaking tasks into smaller steps ⚡"
        color = "🟡"
    else:
        level = "High"
        advice = "High overload detected. Strongly consider rest or reducing demands 🔴"
        color = "🔴"

    st.write(f"### {color} Overload Level: **{level}**")
    st.info(advice)
