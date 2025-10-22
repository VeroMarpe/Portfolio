import streamlit as st

# 📋 Configuración inicial
st.set_page_config(
    page_title="Verónica Martínez — Data Analyst & Consultant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🌍 Idioma actual
LANG = st.session_state.get("lang", "EN")

# 🗺️ Traducciones
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
        "contact": "💬 Info & contact"
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
        "contact": "💬 Información & contacto"
    }
}

# 🏳️ Selector de idioma (banderas)
col_lang1, col_lang2 = st.columns([0.08, 0.9])
with col_lang1:
    if st.button("🇪🇸"):
        st.session_state.lang = "ES"
        st.rerun()
    if st.button("🇬🇧"):
        st.session_state.lang = "EN"
        st.rerun()

lang = st.session_state.get("lang", "EN")
t = translations[lang]

# 🎨 Estilos globales (gris + fuente Forum)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Forum&display=swap');

        [data-testid="stAppViewContainer"] {
            background-color: #F5F5F5 !important;
            font-family: 'Forum', serif !important;
        }
        [data-testid="stSidebar"] {
            background-color: #E0E0E0 !important;
            font-family: 'Forum', serif !important;
        }
        h1, h2, h3, h4, h5, h6, p, span, li, div, label {
            color: #000000 !important;
            font-family: 'Forum', serif !important;
        }
        a {
            color: #2b6cb0 !important;
            text-decoration: none !important;
        }
        a:hover { text-decoration: underline !important; }
    </style>
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
