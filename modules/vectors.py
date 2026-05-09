import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def vector_demo():
    st.header("Vector Similarity Lab")

    mode = st.radio(
        "Choose Input Mode",
        ["Default Example", "Custom Input"]
    )

    if mode == "Default Example":
        v1 = np.array([2, 3])
        v2 = np.array([5, 4])

    else:
        v1 = np.array([
            st.number_input("v1_x", value=2),
            st.number_input("v1_y", value=3)
        ])

        v2 = np.array([
            st.number_input("v2_x", value=5),
            st.number_input("v2_y", value=4)
        ])

    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)

    dot = np.dot(v1, v2)

    cos_sim = dot / (mag1 * mag2)

    st.write(f"Vector 1: {v1}")
    st.write(f"Vector 2: {v2}")

    st.write(f"Magnitude v1: {mag1:.2f}")
    st.write(f"Magnitude v2: {mag2:.2f}")
    st.write(f"Dot Product: {dot:.2f}")
    st.write(f"Cosine Similarity: {cos_sim:.2f}")

    fig, ax = plt.subplots()

    ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1)
    ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid()

    st.pyplot(fig)
