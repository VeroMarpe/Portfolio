import streamlit as st
import yaml
from pathlib import Path

st.set_page_config(page_title="Proyectos — Verónica", page_icon="📁", layout="wide")
st.title("Proyectos")

st.markdown("Explora algunos de mis proyectos destacados en análisis y visualización de datos.")

# Cargar proyectos
proj_path = Path("data/projects.yaml")
projects = yaml.safe_load(proj_path.read_text()) if proj_path.exists() else []

if not projects:
    st.info("Aún no hay proyectos disponibles.")
else:
    cols = st.columns(3)
    for i, p in enumerate(projects):
        with cols[i % 3]:
            st.image(p.get("image"), use_column_width=True)
            st.subheader(p.get("title"))
            st.caption(p.get("summary"))
            if p.get("link_demo"):
                st.markdown(f"[🔗 Ver demo]({p['link_demo']})")
            if p.get("link_github"):
                st.markdown(f"[💻 Ver código]({p['link_github']})")
