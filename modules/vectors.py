# modules/vectors.py

import streamlit as st
import numpy as np
import plotly.graph_objects as go


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

    col1, col2 = st.columns(2)

    col1.metric("Magnitude v1", f"{mag1:.2f}")
    col1.metric("Dot Product", f"{dot:.2f}")

    col2.metric("Magnitude v2", f"{mag2:.2f}")
    col2.metric("Cosine Similarity", f"{cos_sim:.2f}")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[0, v1[0]],
        y=[0, v1[1]],
        mode='lines+markers',
        name='Vector 1'
    ))

    fig.add_trace(go.Scatter(
        x=[0, v2[0]],
        y=[0, v2[1]],
        mode='lines+markers',
        name='Vector 2'
    ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='#0f172a',
        plot_bgcolor='#0f172a',
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)
