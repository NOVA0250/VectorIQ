# modules/bayes.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def bayes_demo():

    st.header("Bayesian Reasoning Lab")

    mode = st.radio(
        "Input Mode",
        ["Default Example", "Custom Input"]
    )

    if mode == "Default Example":

        prior = 0.01
        sensitivity = 0.99
        false_positive = 0.05

    else:

        prior = st.slider(
            "Prior Probability P(D)",
            0.0,
            1.0,
            0.01
        )

        sensitivity = st.slider(
            "Sensitivity P(+|D)",
            0.0,
            1.0,
            0.99
        )

        false_positive = st.slider(
            "False Positive P(+|~D)",
            0.0,
            1.0,
            0.05
        )

    evidence = (
        sensitivity * prior +
        false_positive * (1 - prior)
    )

    posterior = (
        sensitivity * prior
    ) / evidence

    col1, col2 = st.columns(2)

    col1.metric(
        "Prior Probability",
        round(prior,4)
    )

    col2.metric(
        "Posterior Probability",
        round(posterior,4)
    )

    categories = ["Prior","Posterior"]
    values = [prior, posterior]

    fig, ax = plt.subplots(figsize=(7,5))

    ax.bar(
        categories,
        values,
        color=['#6b7280','#d1d5db']
    )

    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    ax.tick_params(colors='white')

    st.pyplot(fig)
