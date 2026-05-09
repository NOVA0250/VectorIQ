# modules/matrix_ops.py

import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def matrix_demo():

    st.header("Matrix Operations Lab")

    operation = st.selectbox(
        "Choose Matrix Operation",
        [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Transpose",
            "Determinant",
            "Inverse",
            "Eigenvalues",
            "Rank",
            "Trace"
        ]
    )

    A = np.array([
        [1,2],
        [3,4]
    ])

    B = np.array([
        [5,6],
        [7,8]
    ])

    if operation == "Addition":
        result = A + B

    elif operation == "Subtraction":
        result = A - B

    elif operation == "Multiplication":
        result = A @ B

    elif operation == "Transpose":
        result = A.T

    elif operation == "Determinant":
        result = np.linalg.det(A)

    elif operation == "Inverse":
        result = np.linalg.inv(A)

    elif operation == "Eigenvalues":
        result = np.linalg.eig(A)[0]

    elif operation == "Rank":
        result = np.linalg.matrix_rank(A)

    elif operation == "Trace":
        result = np.trace(A)

    st.write(result)

    if isinstance(result, np.ndarray):

        fig, ax = plt.subplots(figsize=(6,5))

        sns.heatmap(
            result,
            annot=True,
            cmap='Greys',
            ax=ax
        )

        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#0f172a')

        st.pyplot(fig)
