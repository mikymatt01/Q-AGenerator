import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
import random
import numpy as np
import nltk

nltk.download('punkt')
nltk.download('brown')
nltk.download('wordnet')

from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize

import locale
locale.getpreferredencoding = lambda: "UTF-8"

class Summarizer:
    def __init__(self):
        self.model = T5ForConditionalGeneration.from_pretrained('t5-base')
        self.tokenizer = T5Tokenizer.from_pretrained('t5-base')
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(self.device)
        self.set_seed(42)

    def set_seed(self, seed: int):
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    def postprocesstext(self, content):
        final=""
        for sent in sent_tokenize(content):
            sent = sent.capitalize()
            final = final +" "+sent
        return final


    def summarizer(self, text, model = None, tokenizer = None):
        if(model == None):
            model = self.model
        if(tokenizer == None):
            tokenizer = self.tokenizer
        text = text.strip().replace("\n"," ")
        text = "summarize: "+text
        max_len = 512
        encoding = tokenizer.encode_plus(text,max_length=max_len, pad_to_max_length=False,truncation=True, return_tensors="pt").to(self.device)

        input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

        outs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            early_stopping=True,
            num_beams=3,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            min_length = 75,
            max_length=300
        )

        dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]
        summary = dec[0]
        summary = self.postprocesstext(summary)
        summary= summary.strip()

        return summary

Summary = Summarizer()

