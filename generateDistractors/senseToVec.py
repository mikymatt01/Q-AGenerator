from sense2vec import Sense2Vec
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import wget
import os
from .mmr import mmr

url = 'https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz'
cmd = 'tar -xvf {}'

class S2V:
  def __init__(self):
    self.model= SentenceTransformer('all-MiniLM-L12-v2')
    filename = wget.download(url)
    os.system(cmd.format(filename))
    self.s2v = Sense2Vec().from_disk('s2v_old')
    
  def removeDuplicates(most_similar, originalword):
    distractors = []
    #remove duplicates
    for each_word in most_similar:
      append_word = each_word[0].split("|")[0].replace("_", " ")
      if append_word not in distractors and append_word != originalword:
          distractors.append(append_word)
    return distractors
  
  def get_answer_and_distractor_embeddings(self,answer,candidate_distractors):
    answer_embedding = self.model.encode([answer])
    distractor_embeddings = self.model.encode(candidate_distractors)
    return answer_embedding,distractor_embeddings
  
  def execute(self, originalword):
    word = originalword.lower()
    word = word.replace(" ", "_")
    # Find the best-matching sense for a given word based on the available senses and frequency counts. 
    sense = self.s2v.get_best_sense(word)
    # Get the most similar entries in the table
    most_similar = self.s2v.most_similar(sense, n=20)
    #remove duplicates
    distractors = self.removeDuplicates(most_similar, originalword)
    distractors.insert(0,originalword)
    # encode distractors and answer
    answer_embedd, distractor_embedds = self.get_answer_and_distractor_embeddings(originalword,distractors)
    #Maximal Marginal Relevance origin: https://maartengr.github.io/KeyBERT/api/mmr.html
    final_distractors = mmr(answer_embedd,distractor_embedds,distractors,5)
    filtered_distractors = []

    for dist in final_distractors:
      filtered_distractors.append(dist[0])

    Answer = filtered_distractors[0]
    Filtered_Distractors =  filtered_distractors[1:]
    return {
      "answer": Answer,
      "distractors": Filtered_Distractors
    }

sense2Vec = S2V()
def run(originalword):
  return sense2Vec.execute(originalword)

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Data(BaseModel):
    keyphrase: str

@app.post("/")
async def read_main(data: Data):
    return run(data.keyphrase)