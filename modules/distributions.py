import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def distribution_demo():
    st.header("Distribution Simulation Lab")

    mode = st.radio(
        "Choose Input Mode",
        ["Default Example", "Custom Input"],
        key="dist_mode"
    )

    if mode == "Default Example":
        mean = 0
        std = 2
        size = 1000

    else:
        mean = st.slider("Mean", -10, 10, 0)
        std = st.slider("Std", 1, 10, 2)
        size = st.slider("Sample Size", 100, 10000, 1000)

    data = np.random.normal(mean, std, size)

    st.write(f"Mean: {np.mean(data):.2f}")
    st.write(f"Variance: {np.var(data):.2f}")
    st.write(f"Std: {np.std(data):.2f}")

    fig, ax = plt.subplots()

    sns.histplot(data, kde=True, ax=ax)

    ax.set_title("Gaussian Distribution")

    st.pyplot(fig)
