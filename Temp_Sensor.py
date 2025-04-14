import random
import time

def get_temp():
    #Simulating temp data between 36-38 Degree Celsius
    return round(random.uniform(36.0,38.0),2)

if __name__ == "__main__":
    while True:
        print("Temperature: ", get_temp(), "Degree Celsius")
        time.sleep(1)
