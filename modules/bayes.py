# modules/bayes.py

import streamlit as st


def bayes_demo():

    st.header("Bayesian Reasoning Lab")

    mode = st.radio(
        "Choose Input Mode",
        ["Default Example", "Custom Input"]
    )

    if mode == "Default Example":

        prior = 0.01
        sensitivity = 0.99
        false_positive = 0.05

    else:

        prior = st.slider("Prior P(D)", 0.0, 1.0, 0.01)
        sensitivity = st.slider("Sensitivity P(+|D)", 0.0, 1.0, 0.99)
        false_positive = st.slider("False Positive P(+|~D)", 0.0, 1.0, 0.05)

    evidence = sensitivity * prior + false_positive * (1 - prior)

    posterior = (sensitivity * prior) / evidence

    st.metric("Posterior Probability", f"{posterior:.4f}")

    st.markdown(f"""
    <div class="glass-card">
    <h3>Conceptual Insight</h3>
    <p>
    Prior belief gets updated after observing evidence using Bayes theorem.
    </p>
    </div>
    """, unsafe_allow_html=True)
