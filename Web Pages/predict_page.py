import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()

regressor=data["model"]
le_country=data["le_country"]
le_education=data["le_education"]  


def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.header('''Enter Information to determine Salary''')

    country={
        "United States of America",
        "India",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada",
        "France",
        "Brazil",
        "Spain",
        "Netherlands",
        "Australia",
        "Poland",
        "Italy",
        "Russian Federation ",
        "Sweden",
        "Turkey",
        "Switzerland",
        "Israel",
        "Norway"
    }

    education={
        "Master’s degree", 
        "Bachelor’s degree", 
        "Post grad",
       "Less Than a Bachelor’s"
    }

    countries = st.selectbox("Country", country)
    edulevel = st.selectbox("Education level", education)
    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X=np.array([[countries, edulevel, experience]])
        X[:,0]=le_country.transform(X[:,0])
        X[:,1]=le_education.transform(X[:,1])
        X=X.astype(float)

        salary = regressor.predict(X)

        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
    