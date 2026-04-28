import streamlit as st
import base64
from pathlib import Path
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout


def _img_to_base64(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    return base64.b64encode(p.read_bytes()).decode('utf-8')


def _set_login_type(login_type: str) -> None:
    st.session_state['login_type'] = login_type


def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    left_spacer, col1, mid_gap, col2, right_spacer = st.columns([1, 4, 1, 4, 1])

    teacher_b64 = _img_to_base64("src/images/teacher.png")
    student_b64 = _img_to_base64("src/images/student.png")
    with col1:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class='card teacher-card' style='text-align:center;'>
                  <img src="data:image/png;base64,{teacher_b64}" style="width:140px; display:block; margin:0 auto 1rem auto;" />
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.button(
                "Teacher Portal",
                key="teacher_portal",
                use_container_width=True,
                on_click=_set_login_type,
                args=("Teacher",),
            )

    with col2:
        with st.container(border=True):
            st.markdown(
                f"""
                <div class='card student-card' style='text-align:center;'>
                  <img src="data:image/png;base64,{student_b64}" style="width:140px; display:block; margin:0 auto 1rem auto;" />
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.button(
                "Student Portal",
                key="student_portal",
                use_container_width=True,
                on_click=_set_login_type,
                args=("Student",),
            )