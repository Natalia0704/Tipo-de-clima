 import streamlit as st

st.title ("tipo de clima")

temperatura= st.number_imput ("temperatura",value=30)
humedad=st.number_imput ("humedad",value=70)
llueve=st.number_imput ("llueve", value=0)
if temperatura >=30:
 if humedad >=70:
  clasificacion= "calor humedo"
 else:
  clasificacion= "calor seco"
elif: temperatura >=15:
 if llueve:
    clasificacion= "templado lluvioso"
 else:
    clasificacion = "templado"
else:
clasificacion = "frio"

  
