import RPi.GPIO as GPIO

def setup_pins():
    GPIO.setmode(GPIO.BCM)
    # Add your GPIO pin setups here
    # Example: GPIO.setup(PIN_NUMBER, GPIO.OUT)

def cleanup_gpio():
    GPIO.cleanup()
