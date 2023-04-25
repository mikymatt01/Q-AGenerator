from app import run
import streamlit as st

if __name__ == '__main__':
    print('check 1')
    run("My name is Michele but my friends call me mikymatt")
    print('check 2')
    paragraph = st.text_input("paragraph")
    print('check 3')
    questgen = run(paragraph)
    st.json(questgen)
#    demo = gr.Interface(fn=run, inputs="text", outputs="json")
#    demo.launch()
