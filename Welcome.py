import streamlit as st
import pandas as pd
import numpy as np


st.write('# Welcome to TKkusa Platform!')
st.markdown('---')

col1, col2 = st.columns([1,1])

with col1:
    st.image(r'C:\Users\user\Documents\GitHub\Streamlit_TK\momiji.jpg', width=300)

with col2:
    st.subheader('About Me')
    st.write('**Name**: HO TING-KUAN')
    st.write('**Nationality**: Republic of China')
    st.write('**College**: National Cheng Kung University')
    st.write('**Major**: Computer Science')
    st.write('**Email**: hotkuan0921@gmail.com')
    st.write('**Github**: https://github.com/TKkusa')

st.markdown('---')
st.write('## Tools Now Available')
st.write('### 1. CSV Visuzlizer')
st.write('### 2. Image processing')









