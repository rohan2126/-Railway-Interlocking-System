import RPi.GPIO as GPIO

# Example GPIO pin setup for sensors
SENSOR_PIN = 4

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)

def get_sensor_data():
    setup_gpio()
    # Replace with actual sensor reading logic
    sensor_value = GPIO.input(SENSOR_PIN)
    return sensor_value
