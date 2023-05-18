import requests
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
port_key = os.getenv("PORT_KEY")
summ_key = os.getenv("SUMM_KEY")
ques_key = os.getenv("QUES_KEY")
predict = "/gradio/run/predict"

text = "Many natural language processing and speech recognition techniques need the ability to handle large sequences as inputs and transform them to specific outputs. Traditional approaches, such as recurrent neural networks (RNN) have several shortcomings that prohibit real-world solutions. Transtormers have become the tundamental design piece overcoming most of these limitations, and they have state-of-the-art results. This chapter starts by introducing the sequence-to-sequence models and their limitations. The chapter then lays out various building blocks of transformers such as attention, multi-head attention, positional encodings, residual connections, and encoder-decoder frameworks in a step-by-step manner. All these functional units get detailed treatment from a theoretical and practical perspective for the reader to get a complete handle on the topic. Finally, a real-world case study concludes the chapter by showing the operative aspects, using well-known libraries and datasets."

response = requests.post(f"{base_url}:{summ_key}{predict}", json={
  "data": [
    text,
]}).json()

summarized_text = response['data'][0]

response = requests.post(f"{base_url}:{port_key}{predict}", json={
  "data": [
    text,
    summarized_text,
]}).json()

keyphrase_list = response["data"][0]

for keyphrase in keyphrase_list:
  keyphrase = keyphrase["answer"]
  response = requests.post(f"{base_url}:{ques_key}{predict}", json={
    "data": [
      summarized_text,
      keyphrase,
  ]}).json()

  data = response["data"][0]
  print(data)
  print(keyphrase)
  print()
