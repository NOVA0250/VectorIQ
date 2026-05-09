# modules/vectors.py

import streamlit as st
import numpy as np
import plotly.graph_objects as go


def vector_demo():

    st.header("Vector Intelligence Lab")

    vector_type = st.selectbox(
        "Choose Vector Concept",
        [
            "Magnitude",
            "Dot Product",
            "Cosine Similarity",
            "Unit Vector",
            "Cross Product",
            "Projection"
        ]
    )

    mode = st.radio(
        "Input Mode",
        ["Default Example", "Custom Input"]
    )

    if mode == "Default Example":

        v1 = np.array([2.0, 3.0])
        v2 = np.array([5.0, 4.0])

    else:

        v1 = np.array([
            st.number_input("v1_x", value=2.0),
            st.number_input("v1_y", value=3.0)
        ])

        v2 = np.array([
            st.number_input("v2_x", value=5.0),
            st.number_input("v2_y", value=4.0)
        ])

    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)

    dot = np.dot(v1, v2)

    cos_sim = dot / (mag1 * mag2)

    if vector_type == "Magnitude":

        col1, col2 = st.columns(2)

        col1.metric("Magnitude v1", round(mag1,2))
        col2.metric("Magnitude v2", round(mag2,2))

    elif vector_type == "Dot Product":

        st.metric("Dot Product", round(dot,2))

    elif vector_type == "Cosine Similarity":

        st.metric("Cosine Similarity", round(cos_sim,2))

    elif vector_type == "Unit Vector":

        st.write(v1 / mag1)

    elif vector_type == "Cross Product":

        cross = np.cross(
            np.append(v1,0),
            np.append(v2,0)
        )

        st.write(cross)

    elif vector_type == "Projection":

        proj = (dot / np.dot(v2,v2)) * v2

        st.write(proj)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[0,v1[0]],
        y=[0,v1[1]],
        mode='lines+markers',
        name='Vector 1'
    ))

    fig.add_trace(go.Scatter(
        x=[0,v2[0]],
        y=[0,v2[1]],
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
