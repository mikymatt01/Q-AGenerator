from fastapi import FastAPI
from app import run
import gradio as gr

demo = gr.Interface(fn=run, inputs="text", outputs="json")
app = gr.mount_gradio_app(app, demo, path="/")

