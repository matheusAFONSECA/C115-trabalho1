import streamlit as st
from utils.frontend_utils import send_request, initialize

def main():
    initialize()  # Inicializa as configurações padrões da página

    # Mostrar as opções para o usuário escolher
    if st.button("Telefone"):
        st.switch_page("pages/pages_telefone.py")        

    if st.button("Internet"):
        st.switch_page("pages/pages_internet.py")

    if st.button("Falar com um atendente"):
        st.switch_page("pages/pages_atendente.py")

if __name__ == "__main__":
    main()
