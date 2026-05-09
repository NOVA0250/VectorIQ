# modules/regression.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import (
    LinearRegression,
    Ridge,
    Lasso,
    LogisticRegression
)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def regression_demo():

    st.header("Regression Intelligence Lab")

    regression_type = st.selectbox(
        "Choose Regression Type",
        [
            "Linear Regression",
            "Polynomial Regression",
            "Ridge Regression",
            "Lasso Regression",
            "Logistic Regression"
        ]
    )

    x = np.array([1,2,3,4,5]).reshape(-1,1)

    y = np.array([2,4,5,4,5])

    if regression_type == "Linear Regression":

        model = LinearRegression()

    elif regression_type == "Polynomial Regression":

        model = make_pipeline(
            PolynomialFeatures(degree=2),
            LinearRegression()
        )

    elif regression_type == "Ridge Regression":

        model = Ridge(alpha=1.0)

    elif regression_type == "Lasso Regression":

        model = Lasso(alpha=0.1)

    elif regression_type == "Logistic Regression":

        y = np.array([0,0,1,1,1])

        model = LogisticRegression()

    model.fit(x,y)

    y_pred = model.predict(x)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.scatter(
        x,
        y,
        s=100
    )

    ax.plot(
        x,
        y_pred,
        linewidth=3,
        color='#d1d5db'
    )

    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    st.pyplot(fig)

    if regression_type != "Logistic Regression":

        mse = np.mean((y - y_pred)**2)

        st.metric(
            "MSE",
            round(mse,2)
        )
