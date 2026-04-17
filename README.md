# Healthcare ML Project

End-to-end healthcare data pipeline and machine learning system that predicts patient test results as **Normal**, **Abnormal**, or **Inconclusive**.

## Setup

```bash
uv venv && source .venv/bin/activate
uv pip install -e .
cp .env.example .env
```

## Ingest Data

Place `healthcare_dataset.csv` in `data/raw/`, then:

```bash
python -m scripts.ingest
```

## Train Model

```bash
python -m ml.train
```

## Run API

```bash
python -m app.main
```

## Example Request

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Age": 45,
    "Gender": "Male",
    "Blood Type": "O+",
    "Medical Condition": "Diabetes",
    "Billing Amount": 2000.5,
    "Admission Type": "Emergency",
    "Insurance Provider": "Cigna",
    "Medication": "Aspirin"
  }'
```

## Example Response

```json
{ "predicted_test_result": "Abnormal", "confidence": 0.35}
```

## Weekly Retraining

Configured via Apache Airflow — runs every Saturday at 12:00 noon.
See `airflow/dags/retrain_dag.py`.
