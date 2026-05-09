# modules/regression.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def regression_demo():

    st.header("Linear Regression Lab")

    x = np.array([1,2,3,4,5])
    y = np.array([2,4,5,4,5])

    m, b = np.polyfit(x, y, 1)

    y_pred = m * x + b

    mse = np.mean((y - y_pred) ** 2)

    col1, col2, col3 = st.columns(3)

    col1.metric("Slope", f"{m:.2f}")
    col2.metric("Intercept", f"{b:.2f}")
    col3.metric("MSE", f"{mse:.2f}")

    fig, ax = plt.subplots(figsize=(8,5))

    ax.scatter(x, y, s=100)

    ax.plot(
        x,
        y_pred,
        linewidth=3,
        color='#d1d5db'
    )

    for i in range(len(x)):
        ax.vlines(x[i], y[i], y_pred[i], colors='gray')

    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    ax.tick_params(colors='white')

    st.pyplot(fig)
