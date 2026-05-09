import streamlit as st
from streamlit_option_menu import option_menu

from modules.vectors import vector_demo
from modules.matrix_ops import matrix_demo
from modules.distributions import distribution_demo
from modules.regression import regression_demo

st.set_page_config(
    page_title="VectorIQ",
    layout="wide",
    page_icon="⚔️"
)

st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#0a0a0a,#111827,#1f2937);
}
.stApp {
    background: linear-gradient(135deg,#0a0a0a,#111827,#1f2937);
    color:white;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="VectorIQ",
        options=[
            "Vectors",
            "Matrices",
            "Distributions",
            "Regression"
        ],
        icons=[
            "vector-pen",
            "grid-3x3-gap",
            "bar-chart",
            "graph-up"
        ],
        default_index=0
    )

st.title("⚔️ VectorIQ")

if selected == "Vectors":
    vector_demo()

elif selected == "Matrices":
    matrix_demo()

elif selected == "Distributions":
    distribution_demo()

elif selected == "Regression":
    regression_demo()
