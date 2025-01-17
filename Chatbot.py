#!/usr/bin/env python
# coding=utf-8

"""
* @Author       : JIYONGFENG jiyongfeng@163.com
* @Date         : 2025-01-17 14:47:21
* @Description  :
* @LastEditTime : 2025-01-17 17:13:38
* @LastEditors  : JIYONGFENG jiyongfeng@163.com
* @Copyright (c) 2025 by ZEZEDATA Technology CO, LTD, All Rights Reserved.
"""

from openai import OpenAI
import streamlit as st
from config import settings

openai_api_key = settings.DEEPSEEK_API_KEY
openai_base_url = settings.DEEPSEEK_BASE_URL
model = settings.DEEPSEEK_MODEL

with st.sidebar:
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "你好，我是你的智能助手，请问有什么可以帮您?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key, base_url=openai_base_url)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
            + " 请用中文回答, 不要使用英文,回答尽量简洁,使用标准markdown语法输出结果。",
        }
    )
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model=model, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    with st.chat_message("assistant"):
        st.write(msg)
