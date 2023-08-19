from rake_nltk import Rake
import nltk
nltk.download('stopwords')

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
class KeyExtractor:
    def __init__(self):
        self.model = Rake()
    def get_keywords(self, text):
        # Extraction given the text.
        self.model.extract_keywords_from_text(text)
        # To get keyword phrases ranked highest to lowest.
        imp_keywords = self.model.get_ranked_phrases()[0:4]

        result = []
        for answer in imp_keywords:
            result.append(answer)
        return result
