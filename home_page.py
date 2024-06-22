import os
import streamlit as st
import re


st.set_page_config(page_title="Sakura Notes Home Page", page_icon=None, layout="wide")
st.title("Sakura Notes Home Page")
st.image("./assets/sakura00.png")
# tab_profile, tab_llm_0, tab_llm_1 = st.tabs(["Profile", "LLM_0", "LLM_1"])


# with tab_llm_0:
#     with open(
#         "./Bilibili_Course/LLM/course_notes/Markdown/【序】五分钟了解大语言模型.md",
#         "r",
#         encoding="utf-8",
#     ) as f:
#         content = f.read()
#         st.markdown(content, unsafe_allow_html=True)

# LangChain supports many other chat models. Here, we're using Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.globals import set_verbose, get_verbose

# Example usage
set_verbose(value=True)  # Enable verbose mode

# supports many more optional parameters. Hover on your `ChatOllama(...)`
# class to view the latest available supported parameters
llm = ChatOllama(model="llama3")
prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")

# using LangChain Expressive Language chain syntax
# learn more about the LCEL on
# /docs/concepts/#langchain-expression-language-lcel
chain = prompt | llm | StrOutputParser()

# for brevity, response is printed in terminal
# You can use LangServe to deploy your application for
# production
print(chain.invoke({"topic": "Space travel"}))
