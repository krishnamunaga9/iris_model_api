Sure! Here’s a more concise version of the `README.md` file:

```markdown
# Iris Model API

A Dockerized FastAPI application to serve a RandomForest model trained on the Iris dataset.

## Project Structure

```
iris_model_api/
├── Dockerfile
├── requirements.txt
├── model/
│   ├── model.pkl
│   └── train_model.py
└── app/
    ├── main.py
    └── __init__.py
```

## Setup Instructions

### 1. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn scikit-learn pandas
pip freeze > requirements.txt
```

### 3. Train the Model

```bash
python model/train_model.py
```

### 4. Build and Run Docker Container

```bash
docker build -t iris-model-api .
docker run -p 8000:8000 iris-model-api
```

## API Endpoints

### Health Check

```bash
curl -X GET "http://127.0.0.1:8000/health"
```

### Prediction

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"data\": [[5.1, 3.5, 1.4, 0.2], [6.7, 3.0, 5.2, 2.3]]}"
```

### PowerShell Commands

**Health Check:**

```powershell
Invoke-WebRequest -Uri "http://127.0.0.1:8000/health" -Method Get
```

**Prediction:**

```powershell
$body = @{
    data = @(
        @(5.1, 3.5, 1.4, 0.2),
        @(6.7, 3.0, 5.2, 2.3)
    )
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://127.0.0.1:8000/predict" -Method Post -ContentType "application/json" -Body $body
```
