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
st.write("---") 

st.subheader("👕 Personaliza tu Recomendación")

col1, col2 = st.columns(2)
with col1:
    genero = st.radio("Selecciona tu género:", ["Mujer", "Hombre"])
with col2:
    estilo = st.radio("Elige tu estilo:", ["Deportivo", "Casual", "Formal"])

if st.button("Ver Recomendación"):
    
    if clasificacion == "calor humedo" or clasificacion == "calor seco":
        if estilo == "Deportivo":
            recomendacion = "Shorts y playera sin mangas."
            imagen = "link_imagen_calor_deportivo.jpg" 
        elif estilo == "Casual":
            recomendacion = "Ropa ligera de algodón o lino."
            imagen = "link_imagen_calor_casual.jpg"
        else:
            recomendacion = "Traje de lino sin corbata."
            imagen = "link_imagen_calor_formal.jpg"
            
    elif clasificacion == "templado" or clasificacion == "templado lluvioso":
         recomendacion = "Pantalón ligero y una chamarra delgada."
         imagen = "link_imagen_templado.jpg"
         
    else: 
         recomendacion = "Abrigo, suéter grueso y bufanda."
         imagen = "link_imagen_frio.jpg"

    st.write(f"Para un estilo **{estilo}** de **{genero}** en clima **{clasificacion}**, te recomendamos:")
    st.info(recomendacion)
    
    

  
