import streamlit as st

# --- Configuración inicial ---
st.set_page_config(layout="wide")

# ======================================================================
# 1. MENÚ LATERAL (SIDEBAR) - SOLO NÚMEROS
# ======================================================================
st.sidebar.markdown("### Ciudad\n**Chihuahua**")
# El usuario solo mueve estos controles, el sistema hace el resto[cite: 14]
temperatura = st.sidebar.number_input("Temperatura (°C)", value=29)
humedad = st.sidebar.number_input("Humedad (%)", value=70)
llueve = st.sidebar.number_input("Lluvia (mm)", value=0)

# ======================================================================
# 2. CEREBRO: CLASIFICACIÓN DEL CLIMA Y FONDO DINÁMICO
# ======================================================================

# A) Lógica para clasificar el clima (basada en tus reglas)
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

# B) Lógica para el color de fondo basada en la clasificación[cite: 14]
if "calor" in clasificacion:
    color_hex = "#F9E79F" # Amarillo pastel (soleado/caluroso)
elif "lluvioso" in clasificacion:
    color_hex = "#AED6F1" # Azul pastel (lluvioso)
elif clasificacion == "templado":
    color_hex = "#E5E7E9" # Gris (nublado/agradable)
else:
    color_hex = "#D6EAF8" # Azul muy claro (frío)

# Inyectamos el CSS para pintar el fondo de toda la app[cite: 14]
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color_hex};
        color: #333333; 
    }}
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

# Título principal
st.title("🌤️ Clima Mood: Chihuahua")
st.success(f"El clima actual es: **{clasificacion.upper()}**")

st.write("---") # Línea divisora


# ======================================================================
# 3. SECCIÓN: HIDRATACIÓN (Enseguida, sin botones extra)
# ======================================================================
st.subheader("💧 Nivel de Hidratación")

# Lógica if/else para calcular el agua basada en la temperatura[cite: 14]
if temperatura >= 30:
    litros = "3.0 Litros"
    vasos = "12 Vasos"
elif temperatura >= 25:
    litros = "2.5 Litros"
    vasos = "10 Vasos"
else:
    litros = "2.0 Litros"
    vasos = "8 Vasos"

# Contenedor oscuro con métricas visuales para la hidratación
st.markdown(
    f"""
    <div class='contenedor-oscuro'>
        <div style='text-align: center;'>
            <p style='margin: 0; font-size: 16px; opacity: 0.8;'>Temperatura</p>
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

st.write("---") # Línea divisora


# ======================================================================
# 4. SECCIÓN: RECOMENDACIÓN DE OUTFIT (INTERACTIVO)
# ======================================================================
st.subheader("👕 Personaliza tu Outfit")

col1, col2 = st.columns(2)
with col1:
    genero = st.radio("Selecciona tu género:", ["Mujer", "Hombre"])
with col2:
    estilo = st.radio("Elige tu estilo:", ["Deportivo", "Casual", "Formal"])

if st.button("Ver Recomendación"):
    # Lógica simplificada de ropa basada en la clasificación del clima
    if "calor" in clasificacion:
        recomendacion = "Ropa ligera, shorts o prendas de lino/algodón."
    elif "lluvioso" in clasificacion:
        recomendacion = "No olvides un impermeable, botas para lluvia y paraguas."
    elif clasificacion == "frio":
        recomendacion = "Chamarra o abrigo grueso, suéter, bufanda y guantes."
    else: 
        recomendacion = "Pantalón ligero, playera y una chamarra delgada."
        
    st.write(f"Para un estilo **{estilo}** de **{genero}** en clima **{clasificacion}**, te recomendamos:")
    st.info(recomendacion)
    # st.image("tu_imagen_aqui.jpg") # Descomenta y agrega tu imagen

  
