#!/usr/bin/env python
# coding=utf-8

"""
* @Author       : JIYONGFENG jiyongfeng@163.com
* @Date         : 2025-01-17 15:56:09
* @Description  :
* @LastEditTime : 2025-01-18 01:10:27
* @LastEditors  : JIYONGFENG jiyongfeng@163.com
* @Copyright (c) 2025 by ZEZEDATA Technology CO, LTD, All Rights Reserved.
"""

import streamlit as st
import toml
from config import settings
import traceback
import os

st.title("OpenAI API Settings")

# user input
openai_api_key = st.text_input("OpenAI API Key", value=settings.DEEPSEEK_API_KEY)
openai_base_url = st.text_input("OpenAI Base URL", value=settings.DEEPSEEK_BASE_URL)
openai_model = st.text_input("OpenAI Model", value=settings.DEEPSEEK_MODEL)

if st.button("Save"):
    # save settings to /config/.secrets.toml
    try:
        # check if config/.secrets.toml exists
        if not os.path.exists("config/.secrets.toml"):
            with open("config/.secrets.toml", "w") as f:
                toml.dump({}, f)
        with open("config/.secrets.toml", "r") as f:
            config = toml.load(f)
        with open("config/.secrets.toml", "w") as f:
            config["default"] = {
                "DEEPSEEK_API_KEY": openai_api_key,
                "DEEPSEEK_BASE_URL": openai_base_url,
                "DEEPSEEK_MODEL": openai_model,
            }
            toml.dump(config, f)
            st.success("Settings saved successfully")
    except Exception:
        error_message = traceback.format_exc()
        st.error(f"Failed to save settings: {error_message}")
