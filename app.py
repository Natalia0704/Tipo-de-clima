import streamlit as st
st.title("tipo de clima")
temperatura = st.sidebar.number_input("temperatura", value=30)
humedad = st.sidebar.number_input("humedad", value=70)
llueve = st.sidebar.number_input("llueve", value=0)
if temperatura >= 30:
    if humedad >= 70:
        clasificacion = "calor humedo"
    else:
        clasificacion = "calor seco"
elif temperatura >= 15:
    if llueve:
        clasificacion = "templado lluvioso"
    else:
        clasificacion = "templado"
else:
    clasificacion = "frio"

st.success(f"El clima actual es: **{clasificacion}**")

  
