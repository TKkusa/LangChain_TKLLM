import streamlit as st
from langchain_community.llms import Ollama

llm = Ollama(model='llama2')

def generate_response(text):
    for r in llm.stream(text):
        yield r


st.title('Ask Me Anything')


with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write_stream(generate_response(text))