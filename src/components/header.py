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
    img_col, spacer_col, text_col = st.columns([1, 0.35, 4], gap="small")

    with img_col:
        with open("src/images/image.png", "rb") as img:
            logo_b64 = base64.b64encode(img.read()).decode("utf-8")

        st.markdown(
            f"""
            <div style="width:92px; height:120px; display:flex; align-items:center; justify-content:center; padding:6px; background:#ffffff; border:2px solid #000; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.06); overflow:hidden;">
                <img src='data:image/png;base64,{logo_b64}' style='max-width:100px; max-height:100px; width:auto; height:auto; object-fit:contain; display:block;' />
            </div>
            """,
            unsafe_allow_html=True,
        )

    with spacer_col:
        st.markdown("", unsafe_allow_html=True)

    with text_col:
        st.markdown("<h3 style='margin:0 0 0.1rem 0; color:#6e6e6e; line-height:1; font-size:2.3rem;'>Presenzo</h3>", unsafe_allow_html=True)
        st.markdown("<p style='margin:0; font-size:1.25rem; line-height:1; color:#6e6e6e; font-family: \"Playfair Display\", cursive;'>Welcome to the teacher screen!</p>", unsafe_allow_html=True)

    # Note: the large register paragraph is rendered by the caller below the columns