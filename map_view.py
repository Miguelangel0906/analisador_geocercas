### map_view.py
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
import pandas as pd

def show_map(df: pd.DataFrame):
    if "latitude" not in df.columns or "longitude" not in df.columns:
        st.warning("No se encontraron coordenadas para mostrar en el mapa.")
        return

    selected_name = st.selectbox("Selecciona un punto para centrar el mapa:", df["name"].dropna().unique())
    row = df[df["name"] == selected_name].iloc[0]
    lat = row["latitude"]
    lon = row["longitude"]

    m = folium.Map(location=[lat, lon], zoom_start=17)
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df.iterrows():
        if pd.notnull(row["latitude"]) and pd.notnull(row["longitude"]):
            folium.Marker(
                location=[row["latitude"], row["longitude"]],
                popup=str(row.get("name", "Sin nombre"))
            ).add_to(marker_cluster)

    st_folium(m, width=700, height=500)
