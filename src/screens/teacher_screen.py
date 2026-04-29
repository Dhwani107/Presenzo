import time

import streamlit as st

from src.components.header import render_teacher_header
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from src.ui.base_layout import style_background_dashboard, style_base_layout


def footer_dashboard():
    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)


def header_dashboard():
    render_teacher_header()


def login_teacher(username, password):
    if not username or not password:
        return False

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True

    return False


def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    st.header("Login using password")
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    teacher_username = st.text_input("Enter username", placeholder="ananyaroy")
    teacher_pass = st.text_input("Enter password", type="password", placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Login", icon=":material/passkey:", shortcut="control+enter", use_container_width=True):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("welcome back!", icon="👋")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password combo")

    with btnc2:
        if st.button("Register Instead", type="primary", icon=":material/passkey:", use_container_width=True):
            st.session_state.teacher_login_type = "register"
            st.rerun()

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All Fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False, "Password doesn't match"

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Sucessfully Created! Login Now"
    except Exception:
        return False, "Unexpected Error!"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.session_state["teacher_login_type"] = "login"
            st.rerun()

    st.header("Register your teacher profile")
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    teacher_username = st.text_input("Enter username", placeholder="ananyaroy")
    teacher_name = st.text_input("Enter name", placeholder="Ananya Roy")
    teacher_pass = st.text_input("Enter password", type="password", placeholder="Enter password")
    teacher_pass_confirm = st.text_input("Confirm your password", type="password", placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Register now", icon=":material/passkey:", shortcut="control+enter", use_container_width=True):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button("Login Instead", type="primary", icon=":material/passkey:", use_container_width=True):
            st.session_state.teacher_login_type = "login"
            st.rerun()

    footer_dashboard()


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_login_type" not in st.session_state:
        st.session_state.teacher_login_type = "login"

    if st.session_state.teacher_login_type == "register":
        teacher_screen_register()
    else:
        teacher_screen_login()