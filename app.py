import streamlit as st
from ui import load_css, opening, menu
from games import memory_game, focus_game, reaction_game

st.set_page_config(
    page_title="Brain Pulse",
    page_icon="🧠",
    layout="centered"
)

load_css()

if "page" not in st.session_state:
    st.session_state.page = "home"


if st.session_state.page == "home":
    opening()

elif st.session_state.page == "menu":
    menu()

elif st.session_state.page == "memory":
    memory_game()

elif st.session_state.page == "focus":
    focus_game()

elif st.session_state.page == "reaction":
    reaction_game()
