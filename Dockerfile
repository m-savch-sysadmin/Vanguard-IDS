From python:3.9-slim
WORKDIR /app
RUN pip install requests
COPY . .
CMD ["python", "app.py"]
