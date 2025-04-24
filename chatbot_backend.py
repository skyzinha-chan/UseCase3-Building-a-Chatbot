# 1. Importações necessárias
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_aws import ChatBedrockConverse
import os

# 2. Função para instanciar o modelo ChatBedrockConverse


def demo_chatbot() -> ChatBedrockConverse:
    """
    Instancia e retorna um modelo ChatBedrockConverse com parâmetros padrão.
    """
    demo_llm = ChatBedrockConverse(
        model="amazon.nova-pro-v1:0",
        temperature=0.1,
        max_tokens=1000,
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )
    return demo_llm

# 3. Função para configurar a memória de conversa


def demo_memory(llm: ChatBedrockConverse) -> ConversationSummaryBufferMemory:
    """
    Cria uma memória de buffer com resumo da conversa utilizando o modelo fornecido.
    """
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=2000)
    return memory

# 4. Função para realizar uma conversa com o modelo e memória fornecidos


def demo_conversation(
    input_text: str,
    llm: ChatBedrockConverse,
    memory: ConversationSummaryBufferMemory
) -> str:
    """
    Executa a conversa com base em um input de texto, modelo LLM e memória de conversa.
    Retorna a resposta do modelo.
    """
    llm_conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    chat_reply = llm_conversation.invoke(input_text)
    return chat_reply['response']


# 5. Bloco de execução principal para testes locais
if __name__ == "__main__":
    llm_instance = demo_chatbot()
    memory_instance = demo_memory(llm_instance)

    pergunta = "Qual a capital da França?"
    resposta = demo_conversation(pergunta, llm_instance, memory_instance)

    print("Pergunta:", pergunta)
    print("Resposta:", resposta)
