import streamlit as st 
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


from dotenv import find_dotenv,load_dotenv
load_dotenv(find_dotenv(),override=True)

# now we will taked take prompt
prompt=ChatPromptTemplate.from_messages(
    [
       ( "system","toy are the helpful assistant .please help the user quries."),
       ("user","question:{question}")
    ]
)
def generate_responce(question,api_key,engine,temperature,max_token):
    openai.api_key=api_key
    llm=ChatOpenAI(model=engine)
    Output_Parser=StrOutputParser
    chain=prompt|llm|Output_Parser
    answer=chain.invoke({"question":question})
    return answer

# Streamlit

# title of the App
st.title("My Chatbot with OpenAI")
# sidebar title
st.sidebar.title("setting")
# taking Api key as a input
api_key=st.sidebar.text_input("please put your openAi key",type="password")
# select openAI model 
engine=st.sidebar.selectbox("Select openAI Model",["gpt-4o","gpt-4","gpt-3.5-turbo","gpt-4-turbo"])
# Adjust temperature and token value................(creativity of Model is Called temperature)
temperature=st.sidebar.slider("temperature",min_value=0.0,max_value=1.0,value=0.5)

max_token=st.sidebar.slider("max_token",min_value=100,max_value=300,value=150)

# Main Interface for User Input
st.write("please write you Question")
user_input=st.text_input("your Prompt:")
if user_input and api_key:
    response=generate_responce(user_input,api_key,engine,temperature,max_token)
    st.write(response)

elif user_input:
    st.warning("please enter your openAI API key in sidebar")

else:
    st.write("please enter your Question in Text Box")