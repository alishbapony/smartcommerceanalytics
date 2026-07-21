#Este modulo permite ensablar el resto de componentes en la UI
import streamlit as st
import pandas as pd
#Importamos los componentes reutilizables como librerias locales
from componentes_datos import IngestorDatos
from componetes_prediccion import MotorPrediccion

#Configuramos el nombre de la pagina de nuestra app web
st.set_page_config(page_title="Consola de Componentes Comerciales", layout="wide")
st.title("📦 Ensamblador de componentes: Inteligencia de Negocio")