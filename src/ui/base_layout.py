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

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #f5f1e8 !important;
            border: 1px solid #d6d0c2 !important;
            border-radius: 18px !important;
            padding: 5rem !important;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.40) !important;
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
            font-family: 'Playfair Display', cursive !important;
            font-size: 1.1rem !important;
            line-height: 1.1 !important;
            text-align: center !important;
            color: #4f4f4f !important;
            background-color: #d8d6c8 !important;
           
            border-radius: 12px !important;
            border: 1px solid #b7b4a6 !important;
            padding: 0.55rem 1.1rem !important;
            display: block !important;
            margin: 0 auto !important;
            box-shadow: 0 6px 14px rgba(0, 0, 0, 0.12) !important;
            transition: background-color 0.25s ease-in-out, color 0.25s ease-in-out, border-color 0.25s ease-in-out, transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
        }

        button:hover {
            background-color: #f0efe7 !important;
            color: #2f2f2f !important;
            border-color: #8f8b79 !important;
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 10px 18px rgba(0, 0, 0, 0.18) !important;
        }

        button[kind="secondary"] {
            background-color: #cfcbb7 !important;
            color: #4f4f4f !important;
            border-color: #a9a99a !important;
            transform: translateY(-2px) !important;
        }

        button[kind="secondary"]:hover {
            background-color: #e5e1cf !important;
            color: #262626 !important;
            border-color: #8f8b79 !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] .stImage {
            display: flex !important;
            justify-content: center !important;
        }

        /* fallback card styles using explicit card classes */
        .card {
            background-color: #76b5c5 !important;
            height: 250px !important;
            
            border-radius: 18px !important;
            padding: 1rem !important;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.50) !important;
            margin-bottom: 1rem !important;
        }

        .teacher-card {
            background-color: #76b5c5 !important;
            
        }

        .student-card {
            background-color: #76b5c5 !important;
            
        }

        
        .card-button {
            font-family: 'Playfair Display', cursive !important;
            font-size: 1.05rem !important;
            color: #4f4f4f !important;
            background-color: #cccccc !important;
            border: 1px solid #b7b4a6 !important;
            padding: 0.55rem 1.1rem !important;
            border-radius: 12px !important;
            display: inline-block !important;
            transition: transform 0.25s ease-in-out, box-shadow 0.25s ease-in-out !important;
            text-decoration: none !important;
        }

        .card-button:hover {
            background-color: #f0efe7 !important;
            color: #2f2f2f !important;
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0 10px 18px rgba(0, 0, 0, 0.18) !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )