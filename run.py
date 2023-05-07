from fastapi import FastAPI
import gradio as gr

CUSTOM_PATH = "/gradio"

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "This is your main app"}


io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)