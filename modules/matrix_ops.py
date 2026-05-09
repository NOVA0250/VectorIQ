import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def matrix_demo():
    st.header("Matrix Operations Lab")

    mode = st.radio(
        "Choose Input Mode",
        ["Default Example", "Custom Input"],
        key="matrix_mode"
    )

    if mode == "Default Example":
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])

    else:
        A = np.array([
            [st.number_input("A11", value=1), st.number_input("A12", value=2)],
            [st.number_input("A21", value=3), st.number_input("A22", value=4)]
        ])

        B = np.array([
            [st.number_input("B11", value=5), st.number_input("B12", value=6)],
            [st.number_input("B21", value=7), st.number_input("B22", value=8)]
        ])

    st.write("Matrix A")
    st.write(A)

    st.write("Matrix B")
    st.write(B)

    st.write("Addition")
    st.write(A + B)

    st.write("Matrix Multiplication")
    st.write(A @ B)

    st.write("Transpose")
    st.write(A.T)

    fig, ax = plt.subplots()

    sns.heatmap(A @ B, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)
