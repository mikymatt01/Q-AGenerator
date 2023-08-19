from generateDistractors.senseToVec import S2V
from keyExtractor.keyBert import KeyExtractor
from questionGeneration.questionGeneration import QuestionGeneration
from summarizer.summarizer import Summarizer
import gradio as gr

sense2Vec = S2V()
Key = KeyExtractor()
Question = QuestionGeneration()
Summary = Summarizer()

def run(text):
  result = []
  summarized_text = Summary.summarizer(text)
  imp_keywords = Key.get_keywords(text)

  for answer in imp_keywords:
    ques = Question.get_question(summarized_text,answer)
    distractors = sense2Vec.execute(answer)
    result.append({
        "question": ques,
        "answer": answer.capitalize(),
        "distractors": distractors
    })
  return result

if __name__ == '__main__':
    demo = gr.Interface(fn=run, inputs="text", outputs="json")
    demo.launch()