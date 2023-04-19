FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
