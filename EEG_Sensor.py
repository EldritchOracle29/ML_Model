import random 
import time

def get_eeg_data():
    #Simulating EEG band powers (Alpha, Beta, Theta, Delta)
    alpha = random.uniform(0.5, 15.0) #Example range for alpha waves
    beta = random.uniform(0.5, 15.0) #-//- beta waves
    theta = random.uniform(0.5, 5.0) #-//- theta waves
    delta = random.uniform(0.5, 5.0) #-//- delta waves
    return{"alpha" : round(alpha, 2), "beta" : round(beta, 2), "theta" : round(theta, 2), "delta" : round(delta, 2)}

if __name__ == "__main__":
    while True:
        eeg_data = get_eeg_data()
        print(f"EEG - Alpha: {eeg_data['alpha']} | Beta: {eeg_data['beta']} | Theta: {eeg_data['theta']} | Delta: {eeg_data['delta']}")
        time.sleep(1)
        