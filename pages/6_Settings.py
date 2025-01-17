#!/usr/bin/env python
# coding=utf-8

"""
* @Author       : JIYONGFENG jiyongfeng@163.com
* @Date         : 2025-01-17 15:56:09
* @Description  :
* @LastEditTime : 2025-01-17 17:04:08
* @LastEditors  : JIYONGFENG jiyongfeng@163.com
* @Copyright (c) 2025 by ZEZEDATA Technology CO, LTD, All Rights Reserved.
"""

import streamlit as st
import toml
from config import settings
import traceback

st.title("OpenAI API Settings")

# 从Dynaconf settings中读取OpenAI API Key

openai_api_key = settings.DEEPSEEK_API_KEY
openai_base_url = settings.DEEPSEEK_BASE_URL
openai_model = settings.DEEPSEEK_MODEL

input_api_key = st.text_input("OpenAI API Key", value=openai_api_key)
input_base_url = st.text_input("OpenAI Base URL", value=openai_base_url)
input_model = st.text_input("OpenAI Model", value=openai_model)

if st.button("Save"):
    # save settings to /config/.secrets.toml
    try:
        with open("config/.secrets.toml", "r") as f:
            config = toml.load(f)
        with open("config/.secrets.toml", "w") as f:
            config["default"] = {
                "DEEPSEEK_API_KEY": input_api_key,
                "DEEPSEEK_BASE_URL": input_base_url,
                "DEEPSEEK_MODEL": input_model,
            }
            toml.dump(config, f)
            st.success("Settings saved successfully")
    except Exception:
        error_message = traceback.format_exc()
        st.error(f"Failed to save settings: {error_message}")
