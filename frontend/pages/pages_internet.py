import streamlit as st
from utils.frontend_utils import send_request, initialize


def main():
    
    initialize()  # Inicializa as configurações padrões da página

    try:
        connection, options = send_request(2)  # Display the API message in the frontend

        if connection:
            st.button(options["1"])
            st.button(options["2"])
            st.button(options["3"])
    
    except Exception:
        st.write("Tente novamente mais tarde!")
        

    if st.button("Voltar"):
        st.switch_page("main.py")

if __name__ == "__main__":
    main()
