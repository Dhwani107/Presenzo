import time

import streamlit as st
from PIL import Image
import numpy as np
from src.components.header import render_teacher_header
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from src.ui.base_layout import style_background_dashboard, style_base_layout


def student_screen():



    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    st.header("Login using face recognition", text_alignment="center")
    st.space()
    st.space()

    photo_source=st.camera_input("Position Your face in centre")
    if photo_source:
        np.array(Image.open(photo_source))
