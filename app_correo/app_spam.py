# app_spam.py
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split

df = pd.read_csv("correos_spam_final.csv")
X = df[['palabras_clave', 'enlaces']]
y = df['spam']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
modelo = Perceptron().fit(X_train, y_train)

st.title("Clasificador de Correos Spam")

palabras = st.number_input("Número de palabras clave", min_value=0)
enlaces = st.number_input("Número de enlaces", min_value=0)

if st.button("Clasificar"):
    entrada = np.array([[palabras, enlaces]])
    pred = modelo.predict(entrada)[0]
    resultado = "SPAM" if pred == 1 else "NO SPAM"
    st.success(f"Resultado: {resultado}")
