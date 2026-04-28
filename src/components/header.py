import streamlit as st
import base64
from src.ui.base_layout import style_background_home, style_base_layout


def header_home():
    with open("src/images/image.png", "rb") as img:
        logo_url = base64.b64encode(img.read()).decode("utf-8")

    st.markdown(
        f"""
        <div style="text-align:center;">
        <img src='data:image/png;base64,{logo_url}' style="height:100px; border-color: #060202; border-width: 2px; border-style: solid; border-radius: 5px; background-color: #28231D;" alt="Logo"
        "/>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h1 style='text-align:center;'>Presenzo</h1>",
        unsafe_allow_html=True,
    )

    st.header("Welcome to Presenzo!")