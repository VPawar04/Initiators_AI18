RAPID RESCUE:

This project implements an AI-powered disaster management system to predict and manage the impact of natural disasters such as earthquakes and hurricanes. The system provides real-time disaster predictions based on input parameters and offers precautionary measures to reduce risk. Additionally, it includes a chatbot functionality to assist users with disaster-related information and advice.

Features
Disaster Prediction:

Earthquake Prediction: Predicts earthquake magnitude based on input parameters (latitude, longitude, and depth).
Hurricane Prediction: Predicts hurricane intensity based on input parameters (maximum wind speed and minimum pressure).
Precautionary Measures: Based on predictions, the system provides safety measures to follow during each disaster.
Chatbot:

An AI-based chatbot powered by Google Gemini API that interacts with users to provide disaster-related advice and answers to queries.
Real-Time Disaster Data:

The system accepts real-time data inputs for disaster prediction and delivers immediate predictions and recommendations.
Technologies Used
Backend:

Flask: Web framework for building the REST API and serving the frontend.
NumPy: For numerical computations.
Joblib: For saving and loading trained machine learning models.
Google Gemini API: For chatbot functionalities and conversational AI.
Frontend:

HTML/CSS/JavaScript: Used to create the user interface for disaster prediction and chatbot interactions.

Fetch API: For sending and receiving data from the backend in JSON format.
Machine Learning:

Scikit-learn: For implementing machine learning models (Random Forest Regressor for earthquake and hurricane prediction).
Joblib: For saving and loading trained models for disaster predictions.
Data:

Earthquake Dataset: Contains information about earthquakes (latitude, longitude, depth, magnitude).
Hurricane Dataset: Contains data about hurricanes (maximum wind, minimum pressure, hurricane intensity).


