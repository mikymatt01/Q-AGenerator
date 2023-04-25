from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, util

class SentenceSimilarity:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    def similarity(self, sentences):
        if(len(sentences) < 2):
            raise Exception("Sorry, sentences lenght is not enough")
        #Compute embedding for both lists
        embeddings1 = self.model.encode(sentences[0], convert_to_tensor=True)
        embeddings2 = self.model.encode(sentences[1], convert_to_tensor=True)

        #Compute cosine-similarities
        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        print("{} \t\t {} \t\t Score: {}".format(sentences[0], sentences[1], cosine_scores[0][0]))
        return str(cosine_scores[0][0])