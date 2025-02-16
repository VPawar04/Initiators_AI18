import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("../datasets/earthquake.csv")

# Select features & target
X = df[['Latitude', 'Longitude', 'Depth']]
y = df['Magnitude']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "../models/earthquake.pkl")
print("Earthquake model saved successfully!")
