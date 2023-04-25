# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . .
CMD python3 -m streamlit run main.py
# -m streamlit run