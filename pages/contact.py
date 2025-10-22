import streamlit as st

# --- idioma por query param (GET) ---
qp = st.query_params
if "lang" in qp:
    st.session_state["lang"] = qp["lang"]

lang = st.session_state.get("lang", "EN")

# --- textos ---
translations = {
    "EN": {
        "language": "Language:",
        "title": "Contact",
        "intro": "Want to discuss a project, collaboration, or just exchange ideas about data and strategy?",
        "cta": "Let’s connect:",
        "email": "📧 Email: ",
        "linkedin": "🔗 LinkedIn: "
    },
    "ES": {
        "language": "Idioma:",
        "title": "Contacto",
        "intro": "¿Quieres hablar sobre un proyecto, una colaboración o simplemente intercambiar ideas sobre datos y estrategia?",
        "cta": "Conectemos:",
        "email": "📧 Correo: ",
        "linkedin": "🔗 LinkedIn: "
    }
}
t = translations[lang]

# --- estilos + selector ---
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Forum&display=swap');
[data-testid="stAppViewContainer"] {{ background-color:#F5F5F5 !important; font-family:'Forum', serif !important; }}
[data-testid="stSidebar"] {{ background-color:#E0E0E0 !important; font-family:'Forum', serif !important; }}
h1,h2,h3,h4,h5,h6,p,span,li,div,label {{ color:#000 !important; font-family:'Forum', serif !important; }}
a {{ color:#2b6cb0 !important; text-decoration:none !important; }}
a:hover {{ text-decoration:underline !important; }}
.lang-selector {{ position: fixed; top: 64px; right: 24px; background: rgba(224,224,224,0.9); border: 1px solid #d4d4d4; border-radius: 10px; padding: 6px 10px; z-index: 9999; }}
.lang-selector .label {{ margin-right: 6px; color:#000; }}
.lang-selector a.flag {{ font-size: 20px; margin-left: 6px; }}
</style>

<div class="lang-selector">
    <span class="label">{t["language"]}</span>
    <a class="flag" href="?lang=ES">🇪🇸</a>
    <a class="flag" href="?lang=EN">🇬🇧</a>
</div>
""", unsafe_allow_html=True)

# --- contenido ---
st.title(t["title"])
st.write(t["intro"])
st.write(t["cta"])

st.markdown(f"""
{t["email"]} [veronicamartinez@example.com](mailto:veronicamartinez@example.com)  
{t["linkedin"]} [linkedin.com/in/veronicamartinez](https://linkedin.com/in/veronicamartinez)
""")
