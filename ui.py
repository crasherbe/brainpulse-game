import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def opening():

    st.markdown('<div class="title">BRAIN PULSE</div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("START GAME"):
        st.session_state.page = "menu"


def menu():

    st.title("Game Menu")

    col1,col2 = st.columns(2)

    with col1:
        if st.button("Memory Pattern"):
            st.session_state.page = "memory"

        if st.button("Find Different"):
            st.session_state.page = "focus"

    with col2:
        if st.button("Reaction Tap"):
            st.session_state.page = "reaction"

        if st.button("Back To Home"):
            st.session_state.page = "home"
