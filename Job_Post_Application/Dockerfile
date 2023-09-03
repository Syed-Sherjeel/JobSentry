FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--port", "3000", "--host", "0.0.0.0"]