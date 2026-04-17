import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

PIPELINE_PATH = "models/healthcare_model_pipeline.pkl"
PACKAGE_PATH = "models/healthcare_model.pkl"


def load_artifacts() -> tuple[Pipeline, LabelEncoder]:
    pipeline = joblib.load(PIPELINE_PATH)
    package = joblib.load(PACKAGE_PATH)
    return pipeline, package["label_encoder"]


def predict(input_data: dict, pipeline: Pipeline, le: LabelEncoder) -> str:
    df = pd.DataFrame([input_data])
    encoded = pipeline.predict(df)
    return le.inverse_transform(encoded)[0]
