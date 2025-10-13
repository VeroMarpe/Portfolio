import streamlit as st


st.set_page_config(page_title="Sobre mí — Verónica", page_icon="👤", layout="wide")


st.title("Sobre mí")


left, right = st.columns([2,1])
with left:
    st.markdown(
"""
Soy **Data Analyst** con experiencia en **Python, SQL y Power BI**. Me enfoco en automatizar procesos y crear
visualizaciones claras que reduzcan el tiempo de reporting y faciliten la toma de decisiones.


**Stack**: Python (pandas), SQL, Power BI, GitHub.
**Intereses**: RRHH analytics, control de gestión y reporting de negocio.
"""
    )
    st.page_link("pages/1_Projects.py", label="Ver proyectos →", icon="📁")


with right:
    st.markdown("**Currículum**")
    st.download_button("Descargar CV (PDF)", data=b"", file_name="Veronica_Martinez_CV.pdf")