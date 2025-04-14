import pandas as pd
import pickle

# Load the trained model
with open('stroke_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Simulate sensor data input (replace with real sensor readings)
data = {
    'temperature': [36.8],
    'oxygen': [98],
    'heart_rate': [78],
    'accel_x': [0.03],
    'accel_y': [0.02],
    'accel_z': [1.00],
    'eeg_alpha': [10.5],
    'eeg_beta': [8.2],
    'eeg_theta': [3.1],
    'eeg_delta': [2.7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Make prediction
result = model.predict(df)

# Output prediction
print("Stroke Risk:", "High" if result[0] == 1 else "Low")
