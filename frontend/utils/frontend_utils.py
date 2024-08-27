import requests
import streamlit as st


def send_request(number: int):
    try:
        data = {"escolha": number}

        # Check if 'telefone' resource is available in the API
        response = requests.post("http://localhost:5000/telefonia", json=data)

        if response.status_code == 200:
            api_response = response.json()  # Load the API response into a JSON format
            st.write(api_response["message"])  # Display the API message in the frontend
        else:
            st.write(
                "Serviço indisponível no momento, por favor, tente novamente mais tarde."
            )

    except Exception:
        st.write("Erro ao conectar com o servidor")

        return

    # connection successful
    return True, api_response["options"]


def initialize():
    st.set_page_config(
        page_title="Chatbot de telefonia",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.title("Chatbot de telefonia")
    st.write("Bem-vindo, eu sou um chatbot de telefonia.")
    st.write("Qual dos serviços abaixo você deseja saber sobre o seu usuário?")
