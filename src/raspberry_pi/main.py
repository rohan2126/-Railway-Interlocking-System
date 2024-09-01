import time
import RPi.GPIO as GPIO
from sensor_readings import get_sensor_data
from ai_model.model_training import load_trained_model

# Load the pre-trained AI model
model = load_trained_model('src/ai_model/train_model.pkl')

def monitor_trains():
    while True:
        sensor_data = get_sensor_data()
        prediction = model.predict([sensor_data])

        if prediction == 1:  # Collision detected
            print("Collision Alert! Sending signal to control room.")
            # Send signal to control room or trigger track switching
        else:
            print("All clear, no collision detected.")
        
        time.sleep(2)  # Adjust the interval as needed

if __name__ == "__main__":
    monitor_trains()
