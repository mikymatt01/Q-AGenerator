import json
from summarizer import Summarizer
from keyExtractor import KeyExtractor
from questionGeneration import QuestionGeneration
from textwrap3 import wrap
import gradio as gr
import os
import spacy

nIp = spacy.load("en_core_web_sm")

import en_core_web_sm
nlp = en_core_web_sm.load()

Summary = Summarizer()
Key = KeyExtractor()
Question = QuestionGeneration()

def run(text):
  result = []
  summarized_text = Summary.summarizer(text)
  imp_keywords = Key.get_keywords(text,summarized_text)
  print (imp_keywords)
  for wrp in wrap(summarized_text, 150):
    print (wrp)
    print ("\n")

  for answer in imp_keywords:
    ques = Question.get_question(summarized_text,answer)
    result.append({
        "question": ques,
        "answer": answer.capitalize()
    })
  return result

if __name__ == '__main__':
    demo = gr.Interface(fn=run, inputs="text", outputs="json")
    demo.launch(share=True)