import numpy as np
import pandas as pd
import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Burnout AI",
    page_icon="🔥",
    layout="centered"
)

# ===== SESSION STATE FOR RESET =====
if 'reset_key' not in st.session_state:
    st.session_state.reset_key = 0
if 'form_data' not in st.session_state:
    st.session_state.form_data = None

# ===== INJECT CUSTOM "SEXY" CSS =====
st.markdown(f"""
    <style>
    /* Remove top margin */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }}

    .main {{
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }}
    
    /* Purple/Indigo Title Gradient */
    h1 {{
        background: -webkit-linear-gradient(#6366f1, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        text-align: center;
        font-size: 3rem !important;
        margin-top: 0px !important;
        padding-top: 0px !important;
    }}
    
    label p {{
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }}

    div[data-testid="stForm"] {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
    }}

    /* PREDICT BUTTON - ELECTRIC BLUE */
    button[kind="primary"] {{
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
        border: none !important;
        color: white !important;
        padding: 12px 0px !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        transition: 0.3s !important;
    }}
    
    button[kind="primary"]:hover {{
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.5) !important;
        transform: translateY(-1px);
    }}

    /* CLEAR BUTTON - SLATE WITH BLUE HOVER */
    button[kind="secondary"] {{
        background: rgba(255, 255, 255, 0.05) !important;
        color: #94a3b8 !important;
        border: 1px solid #475569 !important;
        padding: 12px 0px !important;
        border-radius: 12px !important;
        transition: 0.3s !important;
    }}
    
    button[kind="secondary"]:hover {{
        border-color: #3b82f6 !important;
        color: #3b82f6 !important;
        background: rgba(59, 130, 246, 0.05) !important;
    }}

    /* Result Styling */
    .result-box {{
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
        margin-top: 20px;
        font-weight: 800;
    }}
    .risk-low {{ border: 2px solid #22c55e; color: #22c55e; background: rgba(34, 197, 94, 0.1); }}
    .risk-med {{ border: 2px solid #f59e0b; color: #f59e0b; background: rgba(245, 158, 11, 0.1); }}
    .risk-high {{ border: 2px solid #ef4444; color: #ef4444; background: rgba(239, 68, 68, 0.1); }}
    </style>
    """, unsafe_allow_html=True)

# ===== HEADER =====
st.write("<h1>Burnout AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; margin-top: -10px;'>Employee Wellness Predictor</p>", unsafe_allow_html=True)

# ===== INPUT FORM =====
with st.form("burnout_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        day_type = st.selectbox("Day Type", ["", "Weekday", "Weekend"], key=f"day_{st.session_state.reset_key}")
        work_hours = st.number_input("Work Hours", 0.0, 24.0, step=0.1, key=f"work_{st.session_state.reset_key}")
        screen_time = st.number_input("Screen Time (hrs)", 0.0, 24.0, step=0.1, key=f"screen_{st.session_state.reset_key}")
        meetings = st.number_input("Meetings Count", 0, 50, step=1, key=f"meet_{st.session_state.reset_key}")
    
    with col2:
        breaks = st.number_input("Breaks Taken", 0, 20, step=1, key=f"break_{st.session_state.reset_key}")
        after_hours = st.number_input("After-hours Work", 0.0, 12.0, step=0.1, key=f"after_{st.session_state.reset_key}")
        sleep = st.number_input("Sleep Hours", 0.0, 24.0, step=0.1, key=f"sleep_{st.session_state.reset_key}")
        task_rate = st.number_input("Task Rate (0-100)", 0.0, 100.0, step=1.0, key=f"task_{st.session_state.reset_key}")

    st.markdown("<br>", unsafe_allow_html=True)
    
    btn_left, btn_right = st.columns(2)
    with btn_left:
        submitted = st.form_submit_button("Predict Burnout Score", type="primary")
    with btn_right:
        clear_clicked = st.form_submit_button("Clear Form", type="secondary")

# ===== LOGIC =====
if clear_clicked:
    st.session_state.reset_key += 1
    st.session_state.form_data = None
    st.rerun()

if submitted:
    if day_type == "":
        st.error("⚠️ Please select a Day Type.")
    else:
        try:
            # Map day_type to numeric for the model
            day_type_val = 1 if day_type == "Weekday" else 0
            
            data = CustomData(
                day_type=day_type_val,
                work_hours=float(work_hours),
                screen_time_hours=float(screen_time),
                meetings_count=int(meetings),
                breaks_taken=int(breaks),
                after_hours_work=float(after_hours),
                sleep_hours=float(sleep),
                task_completion_rate=float(task_rate)
            )
            
            results = PredictPipeline().predict(data.get_data_as_data_frame())
            score = results[0]

            st.markdown("<br>", unsafe_allow_html=True)
            
            # Risk Level Logic
            if score <= 40:
                risk_class = "risk-low"
                risk_text = "LOW RISK"
            elif score <= 70:
                risk_class = "risk-med"
                risk_text = "MEDIUM RISK"
            else:
                risk_class = "risk-high"
                risk_text = "HIGH RISK"

            st.markdown(f'''
                <div class="result-box {risk_class}">
                    🔥 Predicted Burnout Score: {score:.2f}<br>
                    <span style="font-size: 0.9rem; letter-spacing: 2px;">{risk_text}</span>
                </div>
            ''', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

# ===== FOOTER =====
st.markdown("<br><hr><p style='text-align: center; color: #64748b; font-size: 0.8rem;'>Developed by Dipak Pulami Magar . 2026</p>", unsafe_allow_html=True)