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


def render_teacher_header():
    # Use nested Streamlit columns so the image, title and welcome text are aligned
    img_col, text_col = st.columns([1, 3])

    with img_col:
        with open("src/images/image.png", "rb") as img:
            logo_b64 = base64.b64encode(img.read()).decode("utf-8")

        st.markdown(
            f"""
            <div style="display:inline-block; padding:4px; background:#ffffff; border:2px solid #000; border-radius:8px; box-shadow:0 4px 10px rgba(0,0,0,0.06);">
                <img src='data:image/png;base64,{logo_b64}' style='height:100px; width:auto; display:block; border-radius:4px;' />
            </div>
            """,
            unsafe_allow_html=True,
        )

    with text_col:
        st.markdown("<h3 style='margin:0; color:#6e6e6e;'>Presenzo</h3>", unsafe_allow_html=True)
        st.markdown("<p style='margin:6px 0 0 0; font-size:1.2rem; color:#6e6e6e; font-family: \"Playfair Display\", cursive;'>Welcome to the teacher screen!</p>", unsafe_allow_html=True)

    # Note: the large register paragraph is rendered by the caller below the columns