import streamlit as st


st.title("Martian Rover")

name_of_file = st.text_input("File name")

if name_of_file:
    f = open(name_of_file, "a")

    value = st.number_input("Distance", max_value=100, min_value=10)

    if st.button("add"):
        f.write(str(value) + "\n")

    f.close()

    for no, d in enumerate(open(name_of_file, 'r').readlines()):
        st.write(f"{no+1}: {d}")

    f.close()
