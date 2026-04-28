import streamlit as st

from src.components.header import render_teacher_header
from src.ui.base_layout import style_background_dashboard, style_base_layout


def _render_teacher_register_form():
    with st.form("teacher_register_form", clear_on_submit=False):
        teacher_name = st.text_input("Teacher name", placeholder="Enter your full name")
        teacher_username = st.text_input("Username", placeholder="Create a username")
        teacher_email = st.text_input("Email", placeholder="Enter your email")
        teacher_password = st.text_input("Password", placeholder="Create a password", type="password")
        confirm_password = st.text_input("Confirm password", placeholder="Re-enter your password", type="password")

        action_left, action_right = st.columns(2)
        with action_left:
            submitted = st.form_submit_button("Register Now", use_container_width=True)
        with action_right:
            login_instead = st.form_submit_button("Login Instead", use_container_width=True)

        if submitted:
            if not all([teacher_name, teacher_username, teacher_email, teacher_password, confirm_password]):
                st.error("All fields are required")
            elif teacher_password != confirm_password:
                st.error("Passwords do not match")
            else:
                st.success(f"Teacher profile created for {teacher_name or teacher_username}")

        if login_instead:
            st.session_state["teacher_form_mode"] = "login"
            st.rerun()

def _render_teacher_login_form():
    with st.form("teacher_login_form", clear_on_submit=False):
        teacher_username = st.text_input("Username or Email", placeholder="Enter your username or email")
        teacher_password = st.text_input("Password", placeholder="Enter your password", type="password")

        action_left, action_right = st.columns(2)
        with action_left:
            submitted = st.form_submit_button("Login", use_container_width=True)
        with action_right:
            register_instead = st.form_submit_button("Register Instead", use_container_width=True)

        if submitted:
            if not all([teacher_username, teacher_password]):
                st.error("Both fields are required")
            else:
                st.success(f"Logged in as {teacher_username}")

        if register_instead:
            st.session_state["teacher_form_mode"] = "register"
            st.rerun()


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_form_mode" not in st.session_state:
        st.session_state["teacher_form_mode"] = "register"

    left, right = st.columns([3, 1], gap="large")

    with left:
        render_teacher_header()

    with right:
        st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
        if st.button("Go back to home", key="loginbackbtn"):
            st.session_state["login_type"] = None
            st.rerun()

    if st.session_state["teacher_form_mode"] == "login":
        st.markdown(
            "<p style='margin:32px 0 0 0; font-size:2rem; font-weight:700; color:#21130d; font-family: \"Playfair Display\", cursive;'>Login to your teacher account</p>",
            unsafe_allow_html=True,
        )
        _render_teacher_login_form()
    else:
        st.markdown(
            "<p style='margin:32px 0 0 0; font-size:2rem; font-weight:700; color:#21130d; font-family: \"Playfair Display\", cursive;'>Register your teacher profile to get started..</p>",
            unsafe_allow_html=True,
        )
        _render_teacher_register_form()

def teacher_screen_register():
    teacher_screen()