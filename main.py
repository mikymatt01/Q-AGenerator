from app import run
import streamlit as st

if __name__ == '__main__':
    run("My name is Michele but my friends call me mikymatt")
    paragraph = st.text_input("paragraph")
    questgen = run(paragraph)
    st.json(questgen)
#    demo = gr.Interface(fn=run, inputs="text", outputs="json")
#    demo.launch()
