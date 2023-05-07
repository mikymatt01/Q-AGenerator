# syntax=docker/dockerfile:1
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["python","-u","run.py"]
# CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "80"]
# -m streamlit run