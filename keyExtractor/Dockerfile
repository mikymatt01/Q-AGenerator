# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
# RUN <<EOF
# apt-get update
# apt-get install -y --no-install-recommends git
# EOF
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
# CMD ["python","-u","keyExtractor.py"]
CMD ["uvicorn", "keyExtractor:app", "--host", "0.0.0.0", "--port", "1234"]
# -m streamlit run