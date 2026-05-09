import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, binom, poisson, uniform


def distribution_demo():

    st.header("Probability Distribution Lab")

    dist = st.selectbox(
        "Choose Distribution",
        [
            "Normal",
            "Bernoulli",
            "Binomial",
            "Poisson",
            "Uniform",
            "Exponential"
        ]
    )

    size = st.slider("Sample Size",100,10000,1000)

    if dist == "Normal":

        mean = st.slider("Mean",-10,10,0)
        std = st.slider("Std",1,10,2)

        data = np.random.normal(mean,std,size)

    elif dist == "Bernoulli":

        p = st.slider("Probability",0.0,1.0,0.5)

        data = bernoulli.rvs(p,size=size)

    elif dist == "Binomial":

        n = st.slider("Trials",1,100,10)
        p = st.slider("Probability",0.0,1.0,0.5)

        data = binom.rvs(n,p,size=size)

    elif dist == "Poisson":

        lam = st.slider("Lambda",1,20,5)

        data = poisson.rvs(lam,size=size)

    elif dist == "Uniform":

        data = uniform.rvs(size=size)

    elif dist == "Exponential":

        data = np.random.exponential(scale=1,size=size)

    st.metric("Mean", round(np.mean(data),2))
    st.metric("Variance", round(np.var(data),2))
    st.metric("Std", round(np.std(data),2))

    fig, ax = plt.subplots(figsize=(8,5))

    sns.histplot(data,kde=True,bins=30,color='#9ca3af',ax=ax)

    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    st.pyplot(fig)
