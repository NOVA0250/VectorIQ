# modules/gradient_descent.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def gradient_demo():

    st.header("Gradient Descent Simulator")

    learning_rate = st.slider(
        "Learning Rate",
        0.001,
        1.0,
        0.1
    )

    iterations = st.slider(
        "Iterations",
        5,
        100,
        20
    )

    x = np.linspace(-10, 10, 200)

    y = x ** 2

    current_x = 8

    points_x = []
    points_y = []

    for _ in range(iterations):

        gradient = 2 * current_x

        current_x = (
            current_x -
            learning_rate * gradient
        )

        points_x.append(current_x)
        points_y.append(current_x ** 2)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        x,
        y,
        linewidth=3,
        color='#9ca3af'
    )

    ax.scatter(
        points_x,
        points_y,
        s=80,
        color='#f3f4f6'
    )

    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    ax.tick_params(colors='white')

    st.pyplot(fig)

    st.metric(
        "Final Optimized Value",
        round(current_x,4)
    )
