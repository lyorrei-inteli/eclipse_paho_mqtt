import paho.mqtt.client as paho
from paho import mqtt
import os
from dotenv import load_dotenv
load_dotenv()

broker_address = os.getenv("BROKER_ADDR")
port = 8883
topic = "solar_sensor"
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

def on_message(client, userdata, message):
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")

def on_connect(client, userdata, flags, rc, _):
    print("Conectado com o código de retorno: ", rc)
    client.subscribe(topic)

client = paho.Client(paho.CallbackAPIVersion.VERSION2, "python_subscriber", protocol=paho.MQTTv5)
client.on_connect = on_connect

# Configurações de TLS
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)

client.on_message = on_message

client.connect(broker_address, port=port)

client.loop_forever()
