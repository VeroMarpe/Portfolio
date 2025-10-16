import streamlit as st
from pathlib import Path
import yaml


st.set_page_config(
    page_title="Verónica Martínez — Data Analyst",
    page_icon="📊",
    layout="wide",
    )


# ---- Styles
css_path = Path("assets/styles.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


# ---- Load projects
projects = []
proj_path = Path("data/projects.yaml")
if proj_path.exists():
    projects = yaml.safe_load(proj_path.read_text()) or []


# ---- Header
st.title("Verónica Martínez")
st.subheader("Data Analyst · Python · SQL · Tableau")
st.write(
"""
Analista de datos especializada en **automatización de reporting**, **dashboarding** y **EDA**.
Trabajo con **Python, SQL y Tableau** para convertir datos en decisiones.
"""
)


# ---- CTA buttons
c1, c2, c3 = st.columns([1,1,1])
with c1:
    st.page_link("pages/1_Projects.py", label="Ver proyectos →", icon="📁")
with c2:
    st.page_link("pages/2_Services.py", label="Servicios →", icon="🧩")
with c3:
    st.page_link("pages/4_Contact.py", label="Contacto →", icon="✉️")


st.divider()


# ---- Featured projects grid
st.markdown("### Proyectos destacados")
if not projects:
    st.info("Añade tus proyectos en `data/projects.yaml`.")
else:
# Mostrar 3 primeros
    cols = st.columns(3)
    for i, p in enumerate(projects[:3]):
        with cols[i % 3]:
            st.markdown(f"<div class='block-card'>", unsafe_allow_html=True)
            if p.get("image"):
                st.image(p["image"], use_column_width=True)
        st.markdown(f"**{p['title']}**")
        st.caption(p.get("summary", ""))
# chips
        chips = " ".join([f"<span class='chip'>{t}</span>" for t in p.get("tags", [])])
        st.markdown(chips, unsafe_allow_html=True)
# links
        links = []
        if p.get("link_demo"):
            links.append(f"[Demo]({p['link_demo']})")
        if p.get("link_github"):
            links.append(f"[GitHub]({p['link_github']})")
        if links:
            st.markdown(" · ".join(links))
        if p.get("impact"):
            st.caption(p["impact"])
        st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<div class='footer'>© "+str(st.session_state.get('_year',''))+" Verónica Martínez</div>", unsafe_allow_html=True)