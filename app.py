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
    import streamlit as st
st.set_page_config(layout="wide")
col_menu, col_principal = st.columns([1, 3])

with col_menu:
    st.markdown("### Ciudad\n**Chihuahua**")
    temperatura = st.number_input("Temperatura", value=29)
    lluvia = st.number_input("Lluvia (mm)", value=0)
    estado_clima = st.selectbox("Estado del Clima", ["Soleado", "Lluvioso", "Nublado"])
if estado_clima == "Soleado":
    color_hex = "#F9E79F" 
    sugerencia = "Día soleado, perfecto para actividades al aire libre!"
elif estado_clima == "Lluvioso":
    color_hex = "#AED6F1" 
    sugerencia = "Día lluvioso, ¡no olvides tu paraguas!"
else:
    color_hex = "#E5E7E9" 
    sugerencia = "Día nublado, clima agradable."
st.markdown(
    f"""
    <style>
    .fondo-dinamico {{
        background-color: {color_hex};
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        color: #333333;
    }}
    </style>
    """, unsafe_allow_html=True
)

with col_principal:
    st.markdown(f"""
    <div class="fondo-dinamico">
        <h2>ESTADO: {estado_clima.upper()}</h2>
        <h1 style='font-size: 50px;'>☀️ {temperatura}°C <span style='font-size: 20px; font-weight: normal;'>Humedad 40%</span></h1>
        <p><i>Sugerencia: {sugerencia}</i></p>
        <p style='font-size: 12px;'>Fondo: Dinámico</p>
    </div>
    """, unsafe_allow_html=True)
st.write("---") 
st.subheader("HIDRATACIÓN")
with st.container():
    st.markdown(
        """
        <div style='background-color: #262730; color: white; padding: 20px; border-radius: 5px; display: flex; justify-content: space-around; align-items: center;'>
            <div style='text-align: center;'>
                <p style='margin: 0; font-size: 14px;'>Clima en Chihuahua</p>
                <h1 style='margin: 0;'>29°C</h1>
            </div>
            <div style='text-align: center;'>
                <p style='margin: 0; font-size: 14px;'>Nivel de Hidratación</p>
                <h3 style='margin: 0; display: inline-block; margin-right: 15px;'>2.5 Litros</h3>
                <h3 style='margin: 0; display: inline-block;'>10 Vasos</h3>
            </div>
        </div>
        """, unsafe_allow_html=True
    )

st.write("") 
col_temp, col_wind, col_humidity = st.columns(3)

with col_temp:
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
with col_wind:
    st.metric(label="Wind", value="9 mph", delta="-8%", delta_color="inverse")
with col_humidity:
    st.metric(label="Humidity", value="86%", delta="4%")
st.write("---")
st.markdown("### Markdown\nDisplay string formatted as Markdown.")
st.code('st.markdown("Hello **world**!")') 
st.markdown("### Video Viewer (1080px W - 1920px H)")
st.info("Espacio reservado para st.video('watch_this.mp4')")
    

  
