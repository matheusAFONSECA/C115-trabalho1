import requests
import streamlit as st


def send_request(number: int) -> str:
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

    except Exception as e:
        st.write("Erro ao conectar com o servidor")

        # st.write(e)  # Display the error message in the frontend

    # connection successful
    return True, api_response["options"]