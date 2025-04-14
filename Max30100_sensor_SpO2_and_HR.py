import random
import time

def get_spo2():
    #Simulating SpO2 data between 95% and 100%
    return round(random.uniform(95.0,100.0), 2)

def get_heart_rate():
    #Simulating Heart Rate between 60 BPM to 100BPM
    return random.randint(60, 100)

if __name__ == "__main__":
    while True:
        print(f"Heart Rate: {get_heart_rate()} BPM | SpO2: {get_spo2()}%")
        time.sleep(1)
        