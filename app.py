# app.py

import streamlit as st
from streamlit_option_menu import option_menu

import modules.vectors as vectors
import modules.matrix_ops as matrix_ops
import modules.distributions as distributions
import modules.regression as regression
import modules.bayes as bayes
import modules.gradient_descent as gradient_descent

st.set_page_config(
    page_title="VectorIQ",
    layout="wide",
    page_icon="⚔️"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        linear-gradient(135deg,#0a0a0a,#111827,#1f2937);
    color: white;
}

section[data-testid="stSidebar"] {
    background: rgba(15,15,15,0.85);
    backdrop-filter: blur(20px);
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    border-radius: 18px;
    padding: 15px;
    border: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

st.title("⚔️ VectorIQ")
st.caption("Interactive ML Mathematics & Intuition Visual Lab")

with st.sidebar:

    selected = option_menu(
        menu_title="VectorIQ",
        options=[
            "Vectors",
            "Matrices",
            "Distributions",
            "Regression",
            "Bayes",
            "Gradient Descent"
        ],
        icons=[
            "vector-pen",
            "grid-3x3-gap",
            "bar-chart",
            "graph-up",
            "activity",
            "bezier2"
        ],
        default_index=0
    )

if selected == "Vectors":
    vectors.vector_demo()

elif selected == "Matrices":
    matrix_ops.matrix_demo()

elif selected == "Distributions":
    distributions.distribution_demo()

elif selected == "Regression":
    regression.regression_demo()

elif selected == "Bayes":
    bayes.bayes_demo()

elif selected == "Gradient Descent":
    gradient_descent.gradient_demo()
