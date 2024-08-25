import streamlit as st
from utils.frontend_utils import send_request


def main():
    st.title("Chatbot de telefonia")
    st.write("Bem-vindo, eu sou um chatbot de telefonia.")
    st.write("Qual dos serviços abaixo você deseja saber sobre o seu usuário?")

    # Add a chatbox
    # user_input = st.text_input("Digite sua mensagem")

    # show the user options to choose from
    if st.button("Telefone"):
        connection, options = send_request(1)  # Display the API message in the frontend

        if connection:
            st.button(options["1"])
            st.button(options["2"])
            st.button(options["3"])
        

    if st.button("Internet"):
        send_request(2)  # Display the API message in the frontend

    if st.button("Falar com um atendente"):
        send_request(3)  # Display the API message in the frontend


if __name__ == "__main__":
    main()
