import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Simulate dataset
np.random.seed(42)
n_samples = 1000

data = {
    'temperature': np.random.normal(36.8, 0.5, n_samples),
    'oxygen': np.random.uniform(92, 100, n_samples),
    'heart_rate': np.random.randint(60, 100, n_samples),
    'accel_x': np.random.uniform(-2.0, 2.0, n_samples),
    'accel_y': np.random.uniform(-2.0, 2.0, n_samples),
    'accel_z': np.random.uniform(-2.0, 2.0, n_samples),
    'eeg_alpha': np.random.uniform(0.5, 15.0, n_samples),
    'eeg_beta': np.random.uniform(0.5, 15.0, n_samples),
    'eeg_theta': np.random.uniform(0.5, 5.0, n_samples),
    'eeg_delta': np.random.uniform(0.5, 5.0, n_samples)
}
labels = np.random.randint(0, 2, n_samples)

df = pd.DataFrame(data)
df['stroke'] = labels

X = df.drop('stroke', axis=1)
y = df['stroke']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
with open("stroke_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'stroke_model.pkl'")
