import streamlit as st
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv


load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With OPENAI"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful massistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, api_key, engine, temperature, max_tokens):
    if not api_key:
        raise ValueError("OpenAI API key is required")
    
    client = OpenAI(api_key=api_key)
    llm = ChatOpenAI(model=engine, openai_api_key=api_key, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

## Title of the app
st.title("Chatbot With OpenAI")

## Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

## Select the OpenAI model
engine = st.sidebar.selectbox("Select OpenAI model", ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"])

## Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main interface for user input
st.write("Ask any question")
user_input = st.text_input("You:")

if user_input:
    if not api_key:
        st.warning("Please enter the OpenAI API Key in the sidebar")
    else:
        try:
            response = generate_response(user_input, api_key, engine, temperature, max_tokens)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
else:
    st.write("Please provide a user input")


