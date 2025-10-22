import streamlit as st

# ⚙️ Configuración inicial
st.set_page_config(
    page_title="Verónica Martínez — Data Analyst & Consultant",
    page_icon="📊",
    layout="wide"
)

# 🌍 Estado inicial de idioma y proyecto seleccionado
if "lang" not in st.session_state:
    st.session_state["lang"] = "EN"
if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

def change_language(lang_code):
    st.session_state["lang"] = lang_code
    st.rerun()

lang = st.session_state["lang"]

# 🗺️ Traducciones
translations = {
    "EN": {
        "language": "Language:",
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
        "projects_title": "Projects",
        "projects": {
            "rrhh": "HR Reporting Automation",
            "ecommerce": "E-commerce Dashboard",
            "ine": "Unemployment EDA (INE)"
        }
    },
    "ES": {
        "language": "Idioma:",
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
        "projects_title": "Proyectos",
        "projects": {
            "rrhh": "Automatización de reporting RRHH",
            "ecommerce": "Dashboard de ventas eCommerce",
            "ine": "EDA desempleo (INE)"
        }
    }
}

t = translations[lang]

# 🎨 Estilo global + fuente Forum
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Forum&display=swap');

[data-testid="stAppViewContainer"] {
    background-color:#F5F5F5 !important;
    font-family:'Forum', serif !important;
}
[data-testid="stSidebar"] {
    background-color:#E0E0E0 !important;
    font-family:'Forum', serif !important;
}
h1,h2,h3,h4,h5,h6,p,span,li,div,label {
    color:#000 !important;
    font-family:'Forum', serif !important;
}
a { color:#2b6cb0 !important; text-decoration:none !important; }
a:hover { text-decoration:underline !important; }

/* Selector arriba a la derecha */
.lang-selector {
    position: fixed;
    top: 64px;
    right: 24px;
    background: rgba(224,224,224,0.9);
    border: 1px solid #d4d4d4;
    border-radius: 10px;
    padding: 6px 10px;
    z-index: 9999;
}
.lang-selector span { margin-right: 6px; color:#000; }
</style>
""", unsafe_allow_html=True)

# 🌐 Selector idioma
st.markdown(f'<div class="lang-selector"><span>{t["language"]}</span></div>', unsafe_allow_html=True)
col_flag_es, col_flag_en = st.columns([0.93, 0.07])
with col_flag_en:
    if st.button("🇪🇸" if lang == "EN" else "🇬🇧"):
        change_language("ES" if lang == "EN" else "EN")

# 🧭 Cabecera principal
st.title(t["title"])
st.subheader(t["subtitle"])
st.write(t["intro"])

st.divider()

# 🧱 Layout de proyectos (izquierda miniaturas, derecha detalle)
col1, col2 = st.columns([1, 2])
col1.header(t["projects_title"])

# --- proyectos (miniaturas clicables)
projects_info = {
    "rrhh": {
        "img": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?w=400",
        "desc": "Automated HR dashboards and KPI reporting using Python + SQL + Power BI."
    },
    "ecommerce": {
        "img": "https://images.unsplash.com/photo-1518779578993-ec3579fee39f?w=400",
        "desc": "E-commerce performance dashboard with cohort, RFM, and margin analysis."
    },
    "ine": {
        "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=400",
        "desc": "EDA and visualization of Spanish unemployment data from INE."
    }
}

# --- miniaturas
for key, name in t["projects"].items():
    if col1.button(name, key=key):
        st.session_state["selected_project"] = key

# --- detalle dinámico del proyecto
selected = st.session_state["selected_project"]

if selected:
    p = projects_info[selected]
    col2.image(p["img"], use_container_width=True)
    col2.write(p["desc"])
else:
    col2.info("👈 " + ("Select a project to explore" if lang == "EN" else "Selecciona un proyecto para explorarlo"))
