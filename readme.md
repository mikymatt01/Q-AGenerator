# QA Generator  

This service generates multiple-choice questions (MCQs) from generic text using three key modules:  

- **Keyword Extractor** – Identifies important keywords from a passage.  
- **Question Generator** – Creates a question based on a keyword and its passage.  
- **Distractor Generator** – Produces plausible but incorrect answer choices.  

## Project Structure  

The GitHub repository is organized into three branches, each corresponding to a different keyword extraction method.  

### **Keyword Extraction**  

Three different approaches have been implemented to extract key phrases:  

- **KeyBERT** [[1]](#1) – Uses BERT-based embeddings.  
- **MultipartiteGraph** [[2]](#2) – Leverages graph-based ranking.  
- **RAKE** [[3]](#3) – A rapid automatic keyword extraction technique.  

### **Distractor Generation**  

This module generates incorrect but contextually relevant answer choices using **Sense2Vec**.[[4]](#4)  

### **Question Generation**  

A **T5 Transformer** model, trained on the **SQuAD dataset**, generates questions based on extracted keywords and their passages.  

## Running the Project  

Each module is packaged as a Docker container. To set up the project:  

1. **Build the Docker images** by running:  
   ```sh
   ./build.sh
   ```  
2. **Start the services** with:  
   ```sh
   ./run.sh
   ```  
3. **Verify the setup** by executing:  
   ```sh
   python test.py
   ```  

## References

<a id="1">[1]</a>
Bert: Pre-training of deep bidirectional transformers for language understanding.
Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina(2018).

<a id="2">[2]</a>
Unsupervised keyphrase extraction with multipartite graphs. Boudin, Florian(2018).

<a id="3">[3]</a>
Automatic keyword extraction from individual documents. Rose, Stuart and Engel, Dave and Cramer, Nick and Cowley, Wendy(2010).

<a id="4">[4]</a>
sense2vec-a fast and accurate method for word sense disambiguation in neural word embeddings. sTrask, Andrew and Michalak, Phil and Liu, John(2015).
