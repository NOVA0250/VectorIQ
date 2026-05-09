# modules/distributions.py

import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def distribution_demo():

    st.header("Distribution Simulation Lab")

    mode = st.radio(
        "Choose Input Mode",
        ["Default Example", "Custom Input"]
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

    col1, col2, col3 = st.columns(3)

    col1.metric("Mean", f"{np.mean(data):.2f}")
    col2.metric("Variance", f"{np.var(data):.2f}")
    col3.metric("Std", f"{np.std(data):.2f}")

    fig, ax = plt.subplots(figsize=(8,5))

    sns.histplot(
        data,
        kde=True,
        bins=30,
        color='#9ca3af',
        ax=ax
    )

    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    ax.tick_params(colors='white')

    st.pyplot(fig)
