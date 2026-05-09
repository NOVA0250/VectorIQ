# app.py

import streamlit as st
from streamlit_option_menu import option_menu

from modules.vectors import vector_demo
from modules.matrix_ops import matrix_demo
from modules.distributions import distribution_demo
from modules.bayes import bayes_demo
from modules.regression import regression_demo
from modules.gradient_descent import gradient_demo

st.set_page_config(
    page_title="VectorIQ",
    layout="wide",
    page_icon="⚔️",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255,255,255,0.04), transparent 25%),
        radial-gradient(circle at bottom right, rgba(255,255,255,0.03), transparent 20%),
        linear-gradient(135deg, #0a0a0a 0%, #111827 50%, #1f2937 100%);
    color: #f3f4f6;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

section[data-testid="stSidebar"] {
    background: rgba(15,15,15,0.75);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.08);
}

h1 {
    font-size: 3rem !important;
    font-weight: 900 !important;
    letter-spacing: -2px;
    color: white;
}

h2, h3 {
    color: #f9fafb;
}

.glass-card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(16px);
    border-radius: 20px;
    padding: 1.2rem;
    border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.35s ease;
}

.glass-card:hover {
    transform: translateY(-6px);
    box-shadow:
        0 0 25px rgba(255,255,255,0.08),
        0 0 60px rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.18);
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
    backdrop-filter: blur(14px);
    transition: 0.3s ease;
}

div[data-testid="stMetric"]:hover {
    transform: scale(1.03);
    box-shadow: 0 0 22px rgba(255,255,255,0.12);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
<h1>⚔️ VectorIQ</h1>
<p style='font-size:18px;color:#d1d5db;'>
Interactive ML Mathematics & Intuition Visual Lab
</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:

    selected = option_menu(
        menu_title="VectorIQ",
        options=[
            "Vectors",
            "Matrices",
            "Distributions",
            "Bayes",
            "Regression",
            "Gradient Descent"
        ],
        icons=[
            "vector-pen",
            "grid-3x3-gap",
            "bar-chart",
            "activity",
            "graph-up",
            "bezier2"
        ],
        default_index=0
    )

if selected == "Vectors":
    vector_demo()

elif selected == "Matrices":
    matrix_demo()

elif selected == "Distributions":
    distribution_demo()

elif selected == "Bayes":
    bayes_demo()

elif selected == "Regression":
    regression_demo()

elif selected == "Gradient Descent":
    gradient_demo()
