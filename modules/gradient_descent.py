import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def gradient_demo():
    st.header("Gradient Descent Simulator")

    learning_rate = st.slider("Learning Rate", 0.001, 1.0, 0.1)

    x = np.linspace(-10, 10, 100)
    y = x ** 2

    current_x = 8

    points_x = []
    points_y = []

    for _ in range(20):
        gradient = 2 * current_x
        current_x = current_x - learning_rate * gradient

        points_x.append(current_x)
        points_y.append(current_x ** 2)

    fig, ax = plt.subplots()

    ax.plot(x, y)
    ax.scatter(points_x, points_y)

    st.pyplot(fig)
