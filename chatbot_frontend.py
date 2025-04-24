import streamlit as st
import chatbot_backend as demo

st.title("Hi, This is Chatbot Talita :sunglasses:")

# Inicializa o LLM e a memória uma única vez na sessão
if 'llm' not in st.session_state:
    st.session_state.llm = demo.demo_chatbot()  # Cria a instância do modelo LLM
    st.session_state.memory = demo.demo_memory(
        st.session_state.llm)  # Passa o LLM para criar a memória

# Inicializa o histórico de chat se não existir
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Re-renderiza o histórico de chat
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Adiciona um botão para limpar o histórico no sidebar
with st.sidebar:
    if st.button("Limpar Histórico"):
        st.session_state.chat_history = []
        st.session_state.memory = demo.demo_memory(
            st.session_state.llm)  # Recria a memória mantendo o mesmo LLM
        st.rerun()

# Campo de entrada do usuário
input_text = st.chat_input(
    "Chat with Bedrock's Udemy Course Bot here. I'm Talita your AI assistant")

if input_text:
    # Exibe a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(input_text)

    # Adiciona ao histórico
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Obtém a resposta do chatbot
    with st.spinner("Pensando..."):
        try:
            chat_response = demo.demo_conversation(
                input_text=input_text,
                llm=st.session_state.llm,  # Usa o LLM da sessão
                memory=st.session_state.memory  # Usa a memória da sessão
            )
        except Exception as e:
            chat_response = f"Desculpe, ocorreu um erro: {str(e)}"

    # Exibe a resposta do assistente
    with st.chat_message("assistant"):
        st.markdown(chat_response)

    # Adiciona a resposta ao histórico
    st.session_state.chat_history.append(
        {"role": "assistant", "text": chat_response})
