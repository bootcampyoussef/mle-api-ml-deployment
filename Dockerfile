FROM python:3.11-slim

WORKDIR /app

# Install the same dependencies used by the local Python workflow.
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy only the API package; MLflow artifacts stay outside the image and are mounted at runtime.
COPY webservice_locally /app/webservice_locally

WORKDIR /app/webservice_locally

EXPOSE 9696

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9696"]
