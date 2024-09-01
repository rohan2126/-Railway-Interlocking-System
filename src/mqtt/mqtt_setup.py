import paho.mqtt.client as mqtt

BROKER = 'localhost'
PORT = 1883
TOPIC = 'railway/interlocking'

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}: {msg.payload.decode()}")

def setup_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    return client

if __name__ == "__main__":
    client = setup_mqtt()
    client.loop_forever()
