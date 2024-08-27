import streamlit as st
from utils.frontend_utils import send_request, initialize


def main():
    initialize()  # Inicializa as configurações padrões da página

    choose_option = str(2)

    try:
        connection, options = send_request(
            choose_option
        )  # Display the API message in the frontend

        if connection:
            if st.button(options["1"]):
                _, __ = send_request(choose_option + options["1"])
            if st.button(options["2"]):
                _, __ = send_request(choose_option + options["2"])
            if st.button(options["3"]):
                _, __ = send_request(choose_option + options["3"])


    except Exception:
        st.write("Tente novamente mais tarde!")

    if st.button("Voltar"):
        st.switch_page("main.py")


if __name__ == "__main__":
    main()
