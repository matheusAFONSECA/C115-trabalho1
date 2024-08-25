import streamlit as st
import requests
from utils.frontend_utils import send_request

def main():
    st.title("Chatbot de telefonia")
    st.write("Bem-vindo, eu sou um chatbot de telefonia.")
    st.write("Qual dos serviços abaixo você deseja saber sobre o seu usuário?")

    # Add a chatbox
    # user_input = st.text_input("Digite sua mensagem")

    # Add three buttons
    if st.button("Telefone"):

        send_request(1)  # Display the API message in the frontend

        # number = 1  # The option chosen by the user
        # data = {'escolha': number}

        # # Check if 'telefone' resource is available in the API
        # response = requests.post("http://localhost:5000/telefonia", json=data)

        # if response.status_code == 200:
        #     api_response = response.json()  # Load the API response into a JSON format
        #     st.write(api_response['message'])  # Display the API message in the frontend
        # else:
        #     st.write("Serviço de telefone indisponível!")

    if st.button("Internet"):
        send_request(2)

    if st.button("Falar com um atendente"):
        send_request(3)
        
if __name__ == '__main__':
    main()
