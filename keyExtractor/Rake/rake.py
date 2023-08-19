from rake_nltk import Rake
import nltk
nltk.download('stopwords')

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
def run(text, summarized_text):
    r = Rake()
    # Extraction given the text.
    r.extract_keywords_from_text(text)
    # To get keyword phrases ranked highest to lowest.
    imp_keywords = r.get_ranked_phrases()[0:4]

    result = []
    for answer in imp_keywords:
        result.append({
            "answer": answer.capitalize()
        })
    return result

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Data(BaseModel):
    text: str
    summarized_text: str

@app.post("/")
async def read_main(data: Data):
    return run(data.text, data.summarized_text)