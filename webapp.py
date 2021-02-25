from model import answer_question
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
import textwrap
import streamlit as st

st.set_page_config(page_title='Machine Learning Q&A App', layout="wide")
st.title('Machine Learning Question Answering App')

article_essay = st.text_area('Enter some text')

# Wrap text to 80 characters.
wrapper = textwrap.TextWrapper(width=80) 
wrapper.fill(article_essay)

question = st.text_input('Enter Question')

answer_ = answer_question(question, article_essay)

st.write(answer_)
