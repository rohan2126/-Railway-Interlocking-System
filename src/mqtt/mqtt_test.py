import paho.mqtt.publish as publish

BROKER = 'localhost'
PORT = 1883
TOPIC = 'railway/interlocking'

if __name__ == "__main__":
    message = "Test message from Railway Interlocking System"
    publish.single(TOPIC, message, hostname=BROKER, port=PORT)
    print("Test message sent!")
