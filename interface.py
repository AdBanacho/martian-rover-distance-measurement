import streamlit as st
from email_send import send_email

st.title("Martian Rover")

name_of_file = st.text_input("File name")

if name_of_file:
    f = open(name_of_file, "a")

    value = st.number_input("Distance", max_value=100, min_value=10)

    col1, col2 = st.columns([3, 1])
    if col1.button("add"):
        f.write(str(value) + "\n")
    if col2.button("send email"):
        send_email(st.secrets["PASS"], name_of_file)

    f.close()

    for no, d in enumerate(open(name_of_file, 'r').readlines()):
        st.write(f"{no+1}: {d}")

    f.close()
