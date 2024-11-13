from llama_cpp import Llama
from prompt_templates import memory_prompt_template
from langchain.chains import LLMChain
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_community.vectorstores import Chroma
from utils import load_config
import chromadb

config = load_config()

def load_ollama_model():
    llm = olama(model=config["ollama_model"])
    return llm

def create_llm(model_path=config["ctransformers"]["model_path"]["large"], 
               model_type=config["ctransformers"]["model_type"]):
    llm = CTransformers(model=model_path, model_type=model_type)
    return llm


def create_embeddings():
    embeddings_path = config["embeddings_path"]
    return HuggingFaceInstructEmbeddings(model_name=embeddings_path)


def create_chat_memory(chat_history):
    return ConversationBufferWindowMemory(memory_key="history", chat_memory=chat_history, k=3)

def create_prompt_from_template(template):
    return PromptTemplate.from_template(template)

def create_llm_chain(llm, chat_prompt):
    return LLMChain(llm=llm, prompt=chat_prompt)
    
def load_normal_chain():
    return chatChain()

def load_vectordb(embeddings):
    chromadb_config = config["chromadb"]
    
    persistent_client = chromadb.PersistentClient(
        path=chromadb_config["chromadb_path"],
    )

    langchain_chroma = Chroma(
        client=persistent_client,
        collection_name=chromadb_config["collection_name"],
        embedding_function=embeddings,
    )

    return langchain_chroma


class chatChain:

    def __init__(self):
        llm = create_llm()
        #llm = load_ollama_model()
        chat_prompt = create_prompt_from_template(memory_prompt_template)
        self.llm_chain = create_llm_chain(llm, chat_prompt)

    def run(self, user_input, chat_history):
        return self.llm_chain.invoke(input={"human_input" : user_input, "history" : chat_history}, stop=["Human:"])["text"]
