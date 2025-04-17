#1 import the ConversationSummaryBufferMemory, ConversationChain, ChatBedrock or ChatBedrockConverse Langchain Modules
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain_aws import ChatBedrockConverse
#2a Write a function for invoking model- client connection with Bedrock with profile, model_id & Inference params- model_kwargs
def demo_chatbot(messages):
    demo_llm=ChatBedrockConverse(
        credentials_profile_name='default',
        model="us.deepseek.r1-v1:0",
        temperature=0.1,
        max_tokens=1000)
    return demo_llm.invoke(messages)
#2b Test out the LLM with invoke method 
messages = [
    {
        "role": "user",
        "content": [{"text": 'What is a Bedrock ? '}],
    }
]
response=demo_chatbot(messages)
print(response)
#3 Create a Function for ConversationBufferMemory (llm and max token limit)
#4 Create a Function for Conversation Chain - Input text + Memory
#5 Chat response using invoke (Prompt template)
#Links :
#https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html
#https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_AmazonTitanText_section.html
#https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-deepseek.html

