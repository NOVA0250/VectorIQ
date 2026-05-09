import streamlit as st

from modules.vectors import vector_demo
from modules.matrix_ops import matrix_demo
from modules.distributions import distribution_demo
from modules.bayes import bayes_demo
from modules.regression import regression_demo
from modules.gradient_descent import gradient_demo

st.set_page_config(page_title="VectorIQ", layout="wide")

st.title("⚔️ VectorIQ")
st.subheader("Interactive ML Mathematics & Intuition Visual Lab")

module = st.sidebar.selectbox(
    "Choose Module",
    [
        "Vectors",
        "Matrices",
        "Distributions",
        "Bayes",
        "Regression",
        "Gradient Descent"
    ]
)

if module == "Vectors":
    vector_demo()

elif module == "Matrices":
    matrix_demo()

elif module == "Distributions":
    distribution_demo()

elif module == "Bayes":
    bayes_demo()

elif module == "Regression":
    regression_demo()

elif module == "Gradient Descent":
    gradient_demo()
