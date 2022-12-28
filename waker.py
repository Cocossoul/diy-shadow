from paho.mqtt import client as mqtt_client
import sys
import os

mac_address = sys.argv[2]
broker = sys.argv[1]
port = 1883
topic = "wol/mqtt"
client_id = 'raspi'
username = sys.argv[3]
password = sys.argv[4]


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def wake_up_gaming_pc(mac_address):
    os.system(f"echo Waking up {mac_address}")
    os.system(f"sudo etherwake -i eth0 {mac_address}")
    return

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' on {msg.topic}")
        if msg.topic == topic and msg.payload.decode() == "wake up":
            wake_up_gaming_pc(mac_address)
        return

    err = client.subscribe(topic)
    if err[0] != 0:
        print("Failed to connect to broker")

    client.on_message = on_message
    return

client = connect_mqtt()
subscribe(client)
client.loop_forever()
