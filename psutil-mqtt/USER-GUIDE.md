# Introduction
Server metrics are collected and published via MQTT with this python server agent. 

# Getting Started
Prerequisite :
- MQTT Broker ([Mosquitto](https://mosquitto.org/), [RabbitMQ with MQTT Plugin](https://www.rabbitmq.com/mqtt.html), [HiveMQ](https://www.hivemq.com/) etc.)
- [Python3](https://www.python.org/) 
- [PIP](https://pypi.org/project/pip/)

Installation :
- Install required dependancies with `pip3 install -r requirements.txt`
- Create a `.env` file that contains these  environment variables `mqttHost` , `mqttPort` , `mqttUser` , `mqttTopic` and `mqttSecrets` 
- Run the python script with `python3 psutil-mqtt.py`

For good code practice and better security, it is advised to store sensitive authentication information in a separate file.

Environment Variables :
- `mqttHost` - IP address for MQTT broker
- `mqttPort` - Port for MQTT
- `mqttUser` - User for connecting to MQTT broker (if any)
- `mqttSecrets` - Password for connecting to MQTT broker (if any)
- `mqttTopic` - User defined topic publishing system resource usage metrics ([best practice](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/mqtt-design-best-practices.html))

For more information about MQTT messaging protocol, please refers to the [official website](https://mqtt.org/) and this excellent [guideline from HiveMQ](https://www.hivemq.com/mqtt-essentials/) . Example environment variables configuration can be found in `.env-example` . 