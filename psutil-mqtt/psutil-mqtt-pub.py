import json
import sys
import os
import dotenv
import psutil
import random
import time
from paho.mqtt import client as mqtt_client

# MQTT Parameters
dotenv.load_dotenv()
broker = os.environ.get("mqttHost")
port = int(os.environ.get("mqttPort"))
topic = os.environ.get("mqttTopic")
client_id = f'hktv-mqtt-{random.randint(0,1000)}'
username = os.environ.get("mqttUser")
password = os.environ.get("mqttSecret")


# Unit Conversion Constants
B2GB = 1024**3
B2MB = 1024**2
sig_fig = 4

# Establish MQTT Connection
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print('Failed to connect, return code %d\n', rc)
    
    #Set Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# Publish System Info JSON Data
def publish(client):
    while True:
        time.sleep(1)
        json_key = {}
        sys_resource(json_key)
        for key in json_key:
            json_key[key] = round(json_key[key], sig_fig)
        msg = json.dumps(json_key)
        result = client.publish(topic,msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to `{topic}`")


def sys_resource(json_key):
    
    #  Create key-value pairs for JSON dump
    json_key['cpu_count'] = psutil.cpu_count()
    json_key['cpu_percent'] = psutil.cpu_percent()

    json_key['mem_total'] = psutil.virtual_memory().total/B2GB # GB
    json_key['mem_used']  = psutil.virtual_memory().used/B2GB # GB 
    json_key['mem_free'] = psutil.virtual_memory().free/B2GB # GB
    json_key['mem_percent'] = psutil.virtual_memory().percent

    json_key['disk_total'] = psutil.disk_usage("/").total/B2GB
    json_key['disk_used'] = psutil.disk_usage("/").used/B2GB
    json_key['disk_free'] = psutil.disk_usage("/").free/B2GB

    json_key['byte_sent'] = psutil.net_io_counters().bytes_sent/B2MB # MB
    json_key['byte_recv'] = psutil.net_io_counters().bytes_recv/B2MB # MB
    json_key['packets_sent'] = psutil.net_io_counters().packets_sent 
    json_key['packets_recv'] = psutil.net_io_counters().packets_recv
    json_key['error_in'] = psutil.net_io_counters().errin
    json_key['error_out'] = psutil.net_io_counters().errout
    json_key['drop_in'] = psutil.net_io_counters().dropin
    json_key['drop_out'] = psutil.net_io_counters().dropout

def main():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    main()