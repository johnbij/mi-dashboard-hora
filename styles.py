import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
            background-color: #f0f2f6;
        }
        .stDownloadButton>button {
            width: 100%;
            background-color: #007bff;
            color: white;
        }
        .stDownloadButton>button:hover {
            background-color: #0056b3;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

