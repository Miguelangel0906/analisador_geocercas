### app.py
import streamlit as st
from geo_data import process_geojson
from map_view import show_map
from exporter import export_excel, export_pdf
from control_panel import upload_file

def run_app():
    geojson_data = upload_file()

    if geojson_data:
        clean_data = process_geojson(geojson_data)
        show_map(clean_data)

        st.subheader("Datos:")
        st.dataframe(clean_data)

        col1, col2 = st.columns(2)
        with col1:
            export_excel(clean_data)
        with col2:
            export_pdf(clean_data)

