import streamlit as st


st.set_page_config(page_title="Contacto — Verónica", page_icon="✉️", layout="wide")


st.title("Contacto")


st.markdown(
"""
¿Te interesa colaborar? Escríbeme por **email** o **LinkedIn**:


- Email: [veronica@example.com](mailto:veronica@example.com)
- LinkedIn: https://www.linkedin.com/in/tu-perfil


También puedo habilitar un formulario aquí si prefieres.
"""
)


with st.expander("Formulario rápido (demo)"):
    with st.form("contact_form"):
        name = st.text_input("Nombre")
        email = st.text_input("Email")
        message = st.text_area("Mensaje")
        sent = st.form_submit_button("Enviar")
        if sent:
            st.success("Gracias, te responderé pronto.")
    # Nota: Para enviar correos reales, integra un backend o servicios como Formspree/Zapier.