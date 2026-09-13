# Minimal image with Python on Alpine
FROM python:3.11-alpine

# Working directory in container
WORKDIR /app

# Copying requirements
COPY requirements.txt .

# Installing requirements in container -> --no-cahce-dir will save space without cache
RUN pip install --no-cache-dir -r requirements.txt

# Copying code
COPY app.py .

# Listening port for app
EXPOSE 8080

# Start the app
CMD ["python", "app.py"]