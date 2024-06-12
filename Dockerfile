FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

EXPOSE 8000

CMD ["python", "json_loader.py"]
