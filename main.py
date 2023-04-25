from fastapi import FastAPI
from app import run
import gradio as gr

demo = gr.Interface(fn=run, inputs="text", outputs="json")
demo.launch(share=True)

