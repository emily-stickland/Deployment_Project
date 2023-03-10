from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle


# Load the saved XGBoost classifier using pickle
with open('final_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask application
loan_app = Flask(__name__)

# Define endpoint for making predictions
@loan_app.route('/predict', methods=['POST'])
def predict():
    # Get data from HTTP request
    data = request.json

    # Make prediction using XGBoost classifier
    prediction = model.predict(data)

    # Return prediction as JSON
    return jsonify(prediction.tolist())

if __name__ == 'main':
    # Run the Flask application
    loan_app.run(host='0.0.0.0', port=5004, debug=True)