import streamlit as st
import json
import os

def upload_file():
    st.sidebar.subheader("Selecciona una fuente de datos")

    opciones = ["Archivo integrado", "Subir archivo"]
    metodo = st.sidebar.radio("Método de carga", opciones)

    if metodo == "Archivo integrado":
        archivos = os.listdir("geojson_files")
        archivo_seleccionado = st.sidebar.selectbox("Selecciona un archivo", archivos)
        ruta = os.path.join("geojson_files", archivo_seleccionado)
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                geojson_data = json.load(f)
                return geojson_data
        except Exception as e:
            st.error(f"Error al cargar el archivo integrado: {e}")

    elif metodo == "Subir archivo":
        uploaded_file = st.sidebar.file_uploader("Sube tu archivo GeoJSON", type=["geojson", "json"])
        if uploaded_file is not None:
            try:
                geojson_data = json.load(uploaded_file)
                return geojson_data
            except Exception as e:
                st.error(f"Error al leer el archivo: {e}")

    return None
