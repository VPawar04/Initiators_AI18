from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set Gemini API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Gemini API key not found. Please set it in your .env file.")

genai.configure(api_key=GEMINI_API_KEY)

# Load the trained models for disaster prediction
try:
    earthquake_model = joblib.load("models/earthquake.pkl")
    hurricane_model = joblib.load("models/hurricane.pkl")
except Exception as e:
    raise ValueError(f"Error loading models: {str(e)}")

# Serve the frontend UI
@app.route("/")
def home():
    return render_template("index.html")

# API Endpoint for earthquake prediction
@app.route("/predict_earthquake", methods=["POST"])
def predict_earthquake():
    try:
        data = request.get_json()
        features = np.array([[data["Latitude"], data["Longitude"], data["Depth"]]])
        prediction = earthquake_model.predict(features)[0]

        # Precautionary measures based on magnitude
        if prediction < 3.0:
            precautionary_measures = "Minor earthquake. No immediate danger, but be alert."
        elif 3.0 <= prediction < 5.0:
            precautionary_measures = "Moderate earthquake. Take cover under sturdy furniture."
        elif 5.0 <= prediction < 7.0:
            precautionary_measures = "Strong earthquake. Evacuate to open areas if safe."
        else:
            precautionary_measures = "Severe earthquake. Seek shelter in a strong, stable structure and avoid bridges."

        return jsonify({"prediction": str(prediction), "precautionary_measures": precautionary_measures})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

# API Endpoint for hurricane prediction
@app.route("/predict_hurricane", methods=["POST"])
def predict_hurricane():
    try:
        data = request.get_json()
        features = np.array([[data["Maximum Wind"], data["Minimum Pressure"]]])
        prediction = hurricane_model.predict(features)[0]

        # Precautionary measures based on wind speed
        if prediction < 50:
            precautionary_measures = "Low wind speed. Stay indoors and monitor weather updates."
        elif 50 <= prediction < 100:
            precautionary_measures = "Moderate wind speed. Secure outdoor objects and stay indoors."
        elif 100 <= prediction < 150:
            precautionary_measures = "Strong wind speed. Evacuate to a safer location if instructed by authorities."
        else:
            precautionary_measures = "Very high wind speed. Seek shelter in a sturdy building and stay away from windows."

        return jsonify({"prediction": str(prediction), "precautionary_measures": precautionary_measures})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

# API Endpoint for Chatbot using Google Gemini API
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")

        if not user_message:
            return jsonify({"error": "Message is required."})

        # Generate chatbot response using Gemini API
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)

        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)