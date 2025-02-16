import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import numpy as np

# Load dataset
df = pd.read_csv("../datasets/hurricane.csv")

# Print column names to debug
print("Available columns in dataset:", df.columns)

# Handle missing values (-999 means missing data)
df.replace(-999, np.nan, inplace=True)
df.dropna(inplace=True)  # Drop rows with missing values

# Select features & target
X = df[['Maximum Wind', 'Minimum Pressure']]  # Corrected column names
y = df['Hurricane Intensity'] if 'Hurricane Intensity' in df.columns else df['Maximum Wind']  # Use Maximum Wind as fallback

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "../models/hurricane.pkl")
print("✅ Hurricane model saved successfully!")
