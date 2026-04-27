import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    left_spacer, col1, mid_gap, col2, right_spacer = st.columns([2, 3, 1, 3, 2])
    with col1:
        if st.button("teacher portal"):
            st.session_state['login_type'] = 'Teacher'
            st.rerun()
    with col2:
        if st.button("student portal"):
            st.session_state['login_type'] = 'Student'
            st.rerun()