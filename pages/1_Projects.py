import streamlit as st
from pathlib import Path
import yaml
import pandas as pd


st.set_page_config(page_title="Proyectos — Verónica", page_icon="📁", layout="wide")


st.title("Proyectos")
st.caption("Explora casos aplicados. Filtra por tecnología o tipo.")


proj_path = Path("data/projects.yaml")
projects = yaml.safe_load(proj_path.read_text()) if proj_path.exists() else []


# --- Filtros
all_tags = sorted({t for p in projects for t in p.get("tags", [])}) if projects else []
selected = st.multiselect("Filtrar por tags", options=all_tags, default=[])


filtered = [p for p in projects if all(t in p.get("tags", []) for t in selected)] if selected else projects


if not filtered:
    st.info("No hay proyectos con esos filtros.")
else:
# Grid responsivo de 3 columnas
    cols = st.columns(3)
    for i, p in enumerate(filtered):
        with cols[i % 3]:
            st.markdown(f"<div class='block-card'>", unsafe_allow_html=True)
            if p.get("image"):
                st.image(p["image"], use_column_width=True)
            st.markdown(f"**{p['title']}**")
            st.caption(p.get("summary", ""))
            chips = " ".join([f"<span class='chip'>{t}</span>" for t in p.get("tags", [])])
            st.markdown(chips, unsafe_allow_html=True)
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


st.divider()


st.subheader("Mini‑demo interactiva: sube un CSV y obtén insights iniciales")
with st.expander("Probar ahora"):
    file = st.file_uploader("Sube un CSV (≤ 10MB)", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write("Shape:", df.shape)
        st.dataframe(df.head(20))
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        if numeric_cols:
            col = st.selectbox("Columna numérica para stats", options=numeric_cols)
            st.write(df[col].describe())