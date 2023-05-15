import requests
from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("BASE_URL")
port_key = os.getenv("PORT_KEY")
summ_key = os.getenv("SUMM_KEY")
ques_key = os.getenv("QUES_KEY")

text = ""

summarized_text = requests.post(f"{base_url}:{summ_key}/gradio/run/predict", json={
  "data": [
    text,
]}).json()

keyphrase = requests.post(f"{base_url}:{port_key}/gradio/run/predict", json={
  "data": [
    summarized_text,
]}).json()

response = requests.post(f"{base_url}:{ques_key}/gradio/run/predict", json={
  "data": [
    response,
]}).json()

print(response)
data = response["data"]
print(data)
