import streamlit as st

def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #76b5c5 !important;
            }

        </style>
        """,
        unsafe_allow_html=True
    )

def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #76b5c5 !important;
            }

        </style>
        """,
        unsafe_allow_html=True
    )

def style_base_layout():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Happy+Monkey&family=Orbitron:wght@400..900&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Sekuya&display=swap');

        header, footer { visibility: hidden; }
        
        .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Playfair Display', cursive !important;
            font-size: 3rem !important;
            line-height: 1 !important;
            text-align: center !important;
            color: #6e6e6e !important;
            font-weight: bolder !important;
            margin: 0 0 1rem 0;
        }

        h1 {
            font-family: 'Playfair Display', cursive !important;
            font-size: 3rem !important;
            line-height: 1 !important;
            text-align: center !important;
            color: #6e6e6e !important;
            font-weight: bolder !important;
            margin-top: 0 !important;
            margin-bottom: 0.5rem !important;
        }

        button
        {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 1.25rem !important;
            line-height: 1 !important;
            text-align: center !important;
            color: #6e6e6e !important;
            background-color: #b7b7b7 !important;
           
            border-radius: 0 !important;
            border: 1px solid #c5c5c5 !important;
            display: block !important;
            margin: 0 auto !important;
            transition: background-color 0.25s ease-in-out, color 0.25s ease-in-out, border-color 0.25s ease-in-out, transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"] {
            background-color: #ccccba !important;
            color: #4f4f4f !important;
            border-color: #a9a99a !important;
            transform: translateY(-2px) !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )