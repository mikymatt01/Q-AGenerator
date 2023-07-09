from nltk.translate import meteor
from nltk import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('wordnet')

#calcola una media tra precision e recall con maggiore enfasi su recall
score = meteor(
[word_tokenize('create or update a vm set')],
word_tokenize('creates or updates a virtual machine scale set')
)

print(f"meteor score: {score}")