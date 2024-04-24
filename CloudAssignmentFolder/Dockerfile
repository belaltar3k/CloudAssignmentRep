FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir nltk

RUN python -m nltk.downloader stopwords punkt

CMD ["python", "CloudPython.py"]
