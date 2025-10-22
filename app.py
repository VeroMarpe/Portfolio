import streamlit as st

# 📋 Configuración inicial
st.set_page_config(
    page_title="Verónica Martínez — Data Analyst & Consultant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🌍 Traducciones
translations = {
    "EN": {
        "title": "Verónica Martínez",
        "subtitle": "Data Analyst & Consultant · Python · SQL · Power BI",
        "intro": (
            "You’re about to make a big move in your company — but you’re not entirely sure if it’s brilliant or a beautiful mess. "
            "That’s where I come in.\n\n"
            "I help teams make **decisions that actually work**, not the kind that only look good on a slide deck.\n\n"
            "And if you’re already in the “wish I could undo that” phase — I have something better than a Ctrl+Z button.\n\n"
            "I **analyze, clean, and automate your data** so it goes from being a problem to being your strongest argument.\n\n"
            "It’s not magic — it’s **structure, clarity, and strategy**, powered by tools I use every day: **Python, SQL, Power BI, and APIs**.\n\n"
            "What makes the difference isn’t the tech itself (though I master it), but **how I use it to validate what truly drives the business**.\n\n"
            "In short: I’m the person who turns chaos into insight — and helps you make sure your next “big step” isn’t a leap into the void."
        ),
        "projects": "📁 View projects",
        "contact": "💬 Info & contact",
        "language": "Language:"
    },
    "ES": {
        "title": "Verónica Martínez",
        "subtitle": "Analista de Datos & Consultora · Python · SQL · Power BI",
        "intro": (
            "Estás a punto de dar un gran paso en tu empresa, pero no tienes del todo claro si es brillante o un caos disfrazado. "
            "Ahí es donde entro yo.\n\n"
            "Ayudo a las empresas a tomar **decisiones que funcionan en la práctica**, no esas que solo se ven bien en una presentación.\n\n"
            "Si ya estás en la fase de “ojalá pudiera volver atrás”, tengo algo mejor que un botón de deshacer.\n\n"
            "**Analizo, limpio y automatizo tus datos** para que pasen de ser un problema a ser tu mejor argumento.\n\n"
            "No es magia: es **estructura, claridad y estrategia**, apoyadas en herramientas que conozco a fondo — **Python, SQL, Power BI y APIs**.\n\n"
            "Lo que me diferencia no es la técnica (aunque la domino), sino **cómo la aplico para validar lo que realmente mueve el negocio**.\n\n"
            "En resumen: soy esa persona que traduce el caos en decisiones con sentido… y que evita que el próximo “gran paso” se convierta en un salto al vacío."
        ),
        "projects": "📁 Ver proyectos",
        "contact": "💬 Información & contacto",
        "language": "Idioma:"
    }
}

# --- idioma por query param (GET) ---
qp = st.query_params
if "lang" in qp:
    st.session_state["lang"] = qp["lang"]

lang = st.session_state.get("lang", "EN")
t = translations[lang]

# 🎨 CSS global + selector arriba derecha
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Forum&display=swap');

[data-testid="stAppViewContainer"] {{
    background-color:#F5F5F5 !important;
    font-family:'Forum', serif !important;
}}
[data-testid="stSidebar"] {{
    background-color:#E0E0E0 !important;
    font-family:'Forum', serif !important;
}}
h1,h2,h3,h4,h5,h6,p,span,li,div,label {{
    color:#000 !important;
    font-family:'Forum', serif !important;
}}
a {{
    color:#2b6cb0 !important;
    text-decoration:none !important;
}}
a:hover {{ text-decoration:underline !important; }}

/* Selector arriba a la derecha */
.lang-selector {{
    position: fixed;
    top: 64px;
    right: 24px;
    background: rgba(224,224,224,0.9);
    border: 1px solid #d4d4d4;
    border-radius: 10px;
    padding: 6px 10px;
    z-index: 9999;
    backdrop-filter: blur(2px);
}}
.lang-selector .label {{ margin-right: 6px; color:#000; }}
.lang-selector a.flag {{
    font-size: 20px;
    margin-left: 6px;
    display: inline-block;
    line-height: 1;
}}
</style>

<div class="lang-selector">
    <span class="label">{t["language"]}</span>
    <a class="flag" href="?lang=ES">🇪🇸</a>
    <a class="flag" href="?lang=EN">🇬🇧</a>
</div>
""", unsafe_allow_html=True)

# 🧭 Contenido principal
st.title(t["title"])
st.subheader(t["subtitle"])
st.write(t["intro"])

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/projects.py", label=t["projects"])
with col2:
    st.page_link("pages/contact.py", label=t["contact"])
