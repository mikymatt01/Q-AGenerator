import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import pke
import traceback
from flashtext import KeywordProcessor

class KeyExtractor:

    def get_nouns_multipartite(self, content):
        out=[]
        try:
            extractor = pke.unsupervised.MultipartiteRank()
            extractor.load_document(input=content,language='en')
            #    not contain punctuation marks or stopwords as candidates.
            pos = {'PROPN','NOUN'}
            #pos = {'PROPN','NOUN'}
            stoplist = list(string.punctuation)
            stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
            stoplist += stopwords.words('english')
            # extractor.candidate_selection(pos=pos, stoplist=stoplist)
            extractor.candidate_selection(pos=pos)
            # 4. build the Multipartite graph and rank candidates using random walk,
            #    alpha controls the weight adjustment mechanism, see TopicRank for
            #    threshold/method parameters.
            extractor.candidate_weighting(alpha=1.1,
                                          threshold=0.75,
                                          method='average')
            keyphrases = extractor.get_n_best(n=15)


            for val in keyphrases:
                out.append(val[0])
        except:
            out = []
            traceback.print_exc()

        return out

    def get_keywords(self, originaltext, summarytext):
      keywords = self.get_nouns_multipartite(originaltext)
      print ("keywords unsummarized: ",keywords)
      keyword_processor = KeywordProcessor()
      for keyword in keywords:
        keyword_processor.add_keyword(keyword)

      keywords_found = keyword_processor.extract_keywords(summarytext)
      keywords_found = list(set(keywords_found))
      print ("keywords_found in summarized: ",keywords_found)

      important_keywords =[]
      for keyword in keywords:
        if keyword in keywords_found:
          important_keywords.append(keyword)

      return important_keywords[:4]