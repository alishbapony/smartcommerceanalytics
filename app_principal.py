#Este modulo permite ensablar el resto de componentes en la UI
import streamlit as st
import pandas as pd
#Importamos los componentes reutilizables como librerias locales
from componentes_datos import IngestorDatos
from componetes_prediccion import MotorPrediccion

#Configuramos el nombre de la pagina de nuestra app web
st.set_page_config(page_title="Consola de Componentes Comerciales", layout="wide")
st.title("📦 Ensamblador de componentes: Inteligencia de Negocio")

#Instanciamos los componentes de forma local 
Ingestor = IngestorDatos()
predictor = MotorPrediccion(incremento_simulado=.20)

#Inicializar el estado de la sesion (session_state)
if 'datos_negocio'not in st.session_state:
    st.session_state.datos_negocio = pd.DataFrame()

# Renderizado Visual
archivo_cargado = st.file_uploader("Cargar archivo de ventas(CSV)", type="csv")

if archivo_cargado:
    try:
        #Usamos el componente de datos para cargar el archiv en el  estado de la memoria.
        st.session_state.datos_negocio = Ingestor.cargar_datos(archivo_cargado)
        st.success("Componente de Datos: Ingesta y Validación exitosa.")
    except Exception as e:
        st.error(f"Fallo de interfaz de datos: (e)")

#Si hay datos en la sesion, los componentes visuales e interactivos se activan 
if not st.session_state.datos_negocio.empty:
    col_tabla, col_prediccion = st.columns(2)

    with col_tabla:
        st.subheader("🗒️ Registro de Ventas")
        st.dataframe(st.session_state.datos_negocio, width="stretch")

    with col_prediccion:
        st.subheader("🔮 Prediccion de stock Requerido")
        #Pasamos los datos limpios de un componente al otro, de forma directa
        df_predicciones = predictor.predecir_demanda(st.session_state.datos_negocio)
        st.dataframe(df_predicciones, width="stretch")