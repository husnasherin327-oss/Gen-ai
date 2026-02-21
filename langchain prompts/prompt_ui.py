from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
import os
import streamlit as st

load_dotenv()
model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=os.getenv("GEMINI_API_KEY")
)

st.header("Research tool")

user_input=st.text_input('Enter your prompt')
if st.button('summarise'):
    result=model.invoke(user_input)
    st.text("some random text")
    st.write(result.content)
print()

