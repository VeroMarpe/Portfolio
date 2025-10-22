import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="Proyectos — Verónica Martínez", page_icon="📁", layout="wide")
st.title("Proyectos")
st.markdown("Algunos proyectos destacados en análisis y visualización de datos:")

proj_file = Path("data/projects.yaml")
if proj_file.exists():
    projects = yaml.safe_load(proj_file.read_text())
else:
    projects = []

if not projects:
    st.info("Aún no hay proyectos disponibles.")
else:
    for p in projects:
        st.divider()
        st.subheader(p.get("title"))
        st.caption(p.get("summary"))
        if p.get("image"):
            st.image(p["image"], use_column_width=True)
        if p.get("link_demo"):
            st.markdown(f"[🔗 Ver demo]({p['link_demo']})")
        if p.get("link_github"):
            st.markdown(f"[💻 Ver código]({p['link_github']})")
        if p.get("impact"):
            st.caption(f"**Impacto:** {p['impact']}")
