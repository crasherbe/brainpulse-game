import streamlit as st
import random
import time


def memory_game():

    st.title("Memory Pattern")

    if "sequence" not in st.session_state:
        st.session_state.sequence = [random.randint(1,9) for _ in range(4)]

    st.write("Ingat angka ini")

    st.write(st.session_state.sequence)

    time.sleep(2)

    st.write(" ")

    guess = st.text_input("Masukkan urutan angka")

    if st.button("Check"):

        seq = "".join(map(str,st.session_state.sequence))

        if guess == seq:
            st.success("Benar")
        else:
            st.error("Salah")

        st.session_state.sequence = [random.randint(1,9) for _ in range(4)]



def focus_game():

    st.title("Find Different")

    numbers = ["8"]*20
    index = random.randint(0,19)
    numbers[index] = "3"

    st.write("Temukan angka berbeda")

    st.write(" ".join(numbers))

    answer = st.number_input("Posisi angka berbeda (1-20)")

    if st.button("Check"):

        if answer-1 == index:
            st.success("Benar")
        else:
            st.error("Salah")



def reaction_game():

    st.title("Reaction Test")

    if st.button("Start"):

        delay = random.randint(2,5)

        time.sleep(delay)

        start = time.time()

        if st.button("CLICK NOW"):

            reaction = time.time()-start

            st.success(f"Reaction Time: {reaction:.3f} seconds")
