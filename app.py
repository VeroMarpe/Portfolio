import streamlit as st

# 📋 Configuración inicial
st.set_page_config(
    page_title="Verónica Martínez — Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Estilos globales (gris claro + fuente Forum)
st.markdown("""
    <style>
        /* Importar fuente Forum desde Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Forum&display=swap');

        /* Fondo principal */
        [data-testid="stAppViewContainer"] {
            background-color: #F5F5F5 !important;
            font-family: 'Forum', serif !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #E0E0E0 !important;
            font-family: 'Forum', serif !important;
        }

        /* Encabezados y texto */
        h1, h2, h3, h4, h5, h6, p, span, li, div, label {
            color: #000000 !important;
            font-family: 'Forum', serif !important;
        }

        /* Enlaces */
        a {
            color: #2b6cb0 !important;
            text-decoration: none !important;
            font-family: 'Forum', serif !important;
        }
        a:hover {
            text-decoration: underline !important;
        }

        /* Botones */
        button[kind="primary"] {
            background-color: #2b6cb0 !important;
            color: white !important;
            border-radius: 6px !important;
            font-family: 'Forum', serif !important;
        }

        /* Cuadros info/warning */
        [data-testid="stAlert"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #E0E0E0 !important;
            font-family: 'Forum', serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🧭 Contenido principal
st.title("Verónica Martínez")
st.subheader("Analista de Datos · Python · SQL · Power BI")

st.write(
    """
Soy analista de datos especializada en **automatización de reporting**, **dashboarding** y **análisis exploratorio**.  
Trabajo con **Python, SQL y Power BI** para transformar datos en decisiones.
    """
)

st.divider()

# 🔗 Enlaces a páginas internas
col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/projects.py", label="📁 Ver proyectos")
with col2:
    st.page_link("pages/contact.py", label="💬 Información & contacto")
