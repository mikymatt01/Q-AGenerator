import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer

class QuestionGeneration:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
        self.tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_squad_v1')
        self.model = self.model.to(self.device)

    def get_question(self, context, answer, model = None, tokenizer = None):
        if(model == None):
            model = self.model
        if(tokenizer == None):
            tokenizer = self.tokenizer
        text = "context: {} answer: {}".format(context,answer)
        encoding = tokenizer.encode_plus(text,max_length=384, pad_to_max_length=False,truncation=True, return_tensors="pt").to(self.device)
        input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

        outs = model.generate(input_ids=input_ids,
            attention_mask=attention_mask,
            early_stopping=True,
            num_beams=5,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            max_length=72
        )

        dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]


        Question = dec[0].replace("question:","")
        Question= Question.strip()
        return Question

Question = QuestionGeneration()

def run(text, answer):
    ques = Question.get_question(text,answer)
    return ques

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Data(BaseModel):
    summarized_text: str
    keyphrase: str
@app.post("/")
async def read_main(data: Data):
    return run(data.summarized_text, data.keyphrase)

