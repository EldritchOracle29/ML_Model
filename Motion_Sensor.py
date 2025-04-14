import random
import time

def get_acc():
    #Simulating accelerometer data for X,Y,Z axes (in g-force)
    x = random.uniform(-2.0,2.0)
    y = random.uniform(-2.0,2.0)
    z = random.uniform(-2.0,2.0)
    return{"x": round(x, 2), "y": round(y, 2), "z": round(z, 2)}

if __name__ == "__main__":
    while True:
        acc_data = get_acc()
        print(f"Accelerometer - X: {acc_data['x']} | Y: { acc_data['y']} | Z: { acc_data['z']}")
        time.sleep(1)
        