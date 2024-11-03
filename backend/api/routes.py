from flask import Blueprint, request, jsonify
from services.model_service import ModelService

api = Blueprint('api', __name__)

model_service = ModelService()

@api.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    prediction, probability = model_service.predict(data)
    
    return jsonify({
        "prediction": int(prediction),
        "probability": probability
    })
