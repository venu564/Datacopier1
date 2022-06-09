from python:3.9

RUN apt update -y && apt install telnet && rm -rf /var/lib/apt/lists/*

RUN mkdir -p data-copier
COPY src data-copier
COPY requirements.txt data-copier

RUN pip install -r data-copier/requirements.txt


