import streamlit as st

def main():
    st.title("Chatbot de telefonia")
    st.write("Bem-vindo, eu sou um chatbot de telefonia. Como posso te ajudar?")
    st.write("Escolha uma das opções abaixo:")

    # Add a chatbox
    # user_input = st.text_input("Digite sua mensagem")

    # Add three buttons
    if st.button("Telefone"):
        st.write("Você escolheu a opção 1!")
    if st.button("Internet"):
        st.write("Você escolheu a opção 2!")
    # if st.button("Opção 3"):
    #     st.write("Você escolheu a opção 3!")

if __name__ == '__main__':
    main()