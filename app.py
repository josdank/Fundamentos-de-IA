import streamlit as st

titulo="Mi primera App"
st.title(titulo)

nombre = st.text_input("Nombre")

# Mostrar el nombre si se ingresó
if st.button("Saludar"):
    if nombre:
        st.write(f"¡Hola, {nombre}")
    else:
        st.warning("Llena el campo")pip install streamlit pandas scikit-learn
