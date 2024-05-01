FROM python:3.10

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000:8000
CMD ["python", "main.py"]
