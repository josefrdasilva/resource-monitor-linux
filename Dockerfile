FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install psutil prometheus_client
CMD ["python", "monitor-python.py"]