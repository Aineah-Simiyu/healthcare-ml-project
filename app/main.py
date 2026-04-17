from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from app.model_loader import init_models, get_pipeline, get_label_encoder
from ml.predict import predict
import os

app = Flask(__name__, static_folder="../frontend")
CORS(app)

init_models()


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/predict", methods=["POST"])
def predict_route():
    body = request.get_json()

    input_data = {
        "Age": body["Age"],
        "Gender": body["Gender"],
        "Blood Type": body["Blood Type"],
        "Medical Condition": body["Medical Condition"],
        "Insurance Provider": body["Insurance Provider"],
        "Billing Amount": body["Billing Amount"],
        "Admission Type": body["Admission Type"],
        "Medication": body["Medication"],
    }

    result = predict(input_data, get_pipeline(), get_label_encoder())
    return jsonify({"predicted_test_result": result, "confidence": 0.35})


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false",).lower() == "true", host='0.0.0.0')
