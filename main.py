import streamlit as st
from app import run_app

# Configuración general de la página
st.set_page_config(page_title="GeoJSON Analyzer", layout="wide")

# Estilos personalizados (CSS)
st.markdown("""
    <style>
        .main {
            background-color: #f2f6fc;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 5%;
            padding-right: 5%;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        h1 {
            color: #1f4e79;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        .stButton>button {
            background-color: #1f4e79;
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
        }
        .stDownloadButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Función principal
def main():
    st.title("📍 Analizador de Geocercas")
    run_app()

if __name__ == "__main__":
    main()
