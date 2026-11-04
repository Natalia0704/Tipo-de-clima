import streamlit as st

# --- Configuración inicial ---
st.set_page_config(layout="wide")

# ======================================================================
# 1. MENÚ LATERAL (SIDEBAR) PARA CAPTURAR DATOS
# ======================================================================
st.sidebar.markdown("### Ciudad\n**Chihuahua**")
temperatura = st.sidebar.number_input("Temperatura (°C)", value=29)
humedad = st.sidebar.number_input("Humedad (%)", value=70)
llueve = st.sidebar.number_input("Lluvia (mm)", value=0)
estado_clima = st.sidebar.selectbox("Estado del Clima", ["Soleado", "Lluvioso", "Nublado"])


# ======================================================================
# 2. CEREBRO Y FONDO DINÁMICO (TODO EL FONDO CAMBIA)
# ======================================================================

# Lógica del if/else para el color de fondo dinámico basado en estado_clima
if estado_clima == "Soleado":
    color_hex = "#F9E79F" # Amarillo pastel
elif estado_clima == "Lluvioso":
    color_hex = "#AED6F1" # Azul pastel
else:
    color_hex = "#E5E7E9" # Gris

# Inyectamos el CSS para pintar el fondo de toda la app (stApp)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color_hex};
        color: #333333; /* Texto oscuro para que se lea bien en el fondo claro */
    }}
    /* Esto es para que el contenedor oscuro de hidratación se mantenga bonito */
    .contenedor-oscuro {{
        background-color: #262730; 
        color: white; 
        padding: 20px; 
        border-radius: 10px; 
        display: flex; 
        justify-content: space-around; 
        align-items: center;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }}
    </style>
    """, unsafe_allow_html=True
)


# Lógica if/else para clasificar el clima (para las recomendaciones)
if temperatura >= 30:
    if humedad >= 70:
        clasificacion = "calor humedo"
    else:
        clasificacion = "calor seco"
elif temperatura >= 15:
    if llueve > 0:
        clasificacion = "templado lluvioso"
    else:
        clasificacion = "templado"
else:
    clasificacion = "frio"

# Título principal
st.title(f"🌤️ Clima Mood: Chihuahua ({estado_clima})")
st.success(f"La clasificación actual es: **{clasificacion}**")

st.write("---") # Línea divisora

# ======================================================================
# 3. SECCIÓN 1: RECOMENDACIÓN DE OUTFIT (INTERACTIVO)
# ======================================================================
st.subheader("👕 Personaliza tu Recomendación")

col1, col2 = st.columns(2)
with col1:
    genero = st.radio("Selecciona tu género:", ["Mujer", "Hombre"])
with col2:
    estilo = st.radio("Elige tu estilo:", ["Deportivo", "Casual", "Formal"])

if st.button("Ver Recomendación"):
    # Lógica simplificada de ropa
    if "calor" in clasificacion:
        recomendacion = "Ropa ligera, shorts o vestidos cortos."
    elif "lluvioso" in clasificacion:
        recomendacion = "No olvides un impermeable o paraguas."
    else:
        recomendacion = "Chamarra o abrigo, bufanda y ropa abrigadora."
        
    st.write(f"Para un estilo **{estilo}** de **{genero}** en clima **{clasificacion}**, te recomendamos:")
    st.info(recomendacion)
    # st.image("tu_imagen_aqui.jpg") # Descomenta cuando tengas la imagen

st.write("---") # Línea divisora


# ======================================================================
# 4. SECCIÓN 2: HIDRATACIÓN ENSEGUIDA
# ======================================================================
st.subheader("💧 Nivel de Hidratación")

# Lógica if/else para calcular el agua[cite: 14]
if temperatura >= 30:
    litros = "3.0 Litros"
    vasos = "12 Vasos"
elif temperatura >= 25:
    litros = "2.5 Litros"
    vasos = "10 Vasos"
else:
    litros = "2.0 Litros"
    vasos = "8 Vasos"

# Contenedor oscuro simulando tu diseño visual[cite: 14]
st.markdown(
    f"""
    <div class='contenedor-oscuro'>
        <div style='text-align: center;'>
            <p style='margin: 0; font-size: 16px; opacity: 0.8;'>Clima Actual</p>
            <h1 style='margin: 0; font-size: 40px;'>{temperatura}°C</h1>
        </div>
        <div style='text-align: center;'>
            <p style='margin: 0; font-size: 16px; opacity: 0.8;'>Tu Meta de Agua</p>
            <h3 style='margin: 0; display: inline-block; margin-right: 20px; font-size: 30px;'>{litros}</h3>
            <h3 style='margin: 0; display: inline-block; font-size: 30px;'>{vasos}</h3>
        </div>
    </div>
    """, unsafe_allow_html=True
)

st.write("") # Espacio
    

  
