import streamlit as st
from utils.frontend_utils import send_request, initialize, options_button


def main():
    initialize()  # Inicializa as configurações padrões da página

    try:
        connection, options = send_request(3)  # Display the API message in the frontend

        if connection:
            options_button(options)

    except Exception:
        st.write("Tente novamente mais tarde!")

    if st.button("Voltar"):
        st.switch_page("main.py")


if __name__ == "__main__":
    main()
