FROM python:3.9-buster
ADD main.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]