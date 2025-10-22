import streamlit as st

st.set_page_config(
    page_title="Verónica Martínez — Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Verónica Martínez")
st.subheader("Analista de Datos · Python · SQL · Power BI")

st.write(
    """
Soy analista de datos especializada en **automatización de reporting**, **dashboarding** y **análisis exploratorio**.  
Trabajo con **Python, SQL y Power BI** para transformar datos en decisiones.
    """
)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/projects.py", label="📁 Ver proyectos")
with col2:
    st.page_link("pages/contact.py", label="💬 Información & contacto")
