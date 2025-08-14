FROM python:3.12-slim


RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "app.py"]