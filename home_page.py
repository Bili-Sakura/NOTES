import os
import streamlit as st
import re


st.set_page_config(page_title="Sakura Notes Home Page", page_icon=None, layout="wide")
st.title("Sakura Notes Home Page")
st.image("./assets/sakura.png")
# tab_profile, tab_llm_0, tab_llm_1 = st.tabs(["Profile", "LLM_0", "LLM_1"])


# with tab_llm_0:
#     with open(
#         "./Bilibili_Course/LLM/course_notes/Markdown/【序】五分钟了解大语言模型.md",
#         "r",
#         encoding="utf-8",
#     ) as f:
#         content = f.read()
#         st.markdown(content, unsafe_allow_html=True)
