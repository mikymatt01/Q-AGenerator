import gradio as gr
from fastapi import FastAPI
from keybert import KeyBERT

CUSTOM_PATH = "/gradio"

app = FastAPI()

kw_model = KeyBERT()

def run(text):
  keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 3), stop_words=None)
  return keywords

@app.get("/")
def read_main():
    return {"message": "This is your main app"}

io = gr.Interface(fn=run, inputs="text", outputs="json")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
