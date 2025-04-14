import time

def buzz(duration = 1):
    #Simulating the buzzer sound
    print(f"BUZZER ON for {duration} second(s)")
    time.sleep(duration)
    print("BUZZER OFF")

if __name__ == "__main__":
    while True:
        buzz(2) #for 2 seconds
        time.sleep(5)