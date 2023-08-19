from keybert import KeyBERT

class KeyExtractor:
    def __init__(self):
        self.model = KeyBERT()

    def get_keywords(self, text):
      keywords = self.model.extract_keywords(text, keyphrase_ngram_range=(1, 3), stop_words=None)
      return keywords

#import gradio as gr
#from fastapi import FastAPI
# CUSTOM_PATH = "/gradio"
# app = FastAPI()
# @app.get("/")
# def read_main():
#     return {"message": "This is your main app"}

# io = gr.Interface(fn=run, inputs="text", outputs="json")
# app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)
