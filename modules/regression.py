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

    st.write(f"Slope: {m:.2f}")
    st.write(f"Intercept: {b:.2f}")
    st.write(f"MSE: {mse:.2f}")

    fig, ax = plt.subplots()

    ax.scatter(x, y)
    ax.plot(x, y_pred, color='red')

    for i in range(len(x)):
        ax.vlines(x[i], y[i], y_pred[i], colors='gray')

    st.pyplot(fig)
