from app import run
import streamlit as st

paragraph = st.text_input("paragraph")
questgen = run(paragraph)
st.json(questgen)

