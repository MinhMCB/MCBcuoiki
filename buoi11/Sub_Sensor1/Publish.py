import paho.mqtt.client as mqtt
import random
import json
from datetime import datetime
from time import sleep
#===========================
# MQTT settings

MQTT_Broker = "localhost" 	# ten may chu
MQTT_Port = 1883		# port mac dinh cua MQTT
Keep_Alive_Interval = 45	# thoi gian gia cac lan gui goi tin
MQTT_Topic = "test"
#==========================
# ham ket noi may chu MQTT

def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print ( "khong the ket noi MQTT...")
	else:
		print("ket noi voi MQTT Broker:" + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass
def on_disconnect(client, userdata, mid):
	if rc !=0:
		pass

mqttc = mqtt.Client()
mqttc.username_pw_set(username="ntm",password="minh6464")	#thay doi user
mqtt.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqtt.on_publish = on_publish
mqttc.connect(MQTT_Broker, MQTT_Port , Keep_Alive_Interval)

#================================
# publish du lieu

def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print(("Published: " + str(message)))
	print("")

#==================================
# fake random sensor


	

while True:
	Humidity_Fake_Value = int(random.uniform(60,100))
	Temperature_Fake_Value = int(random.uniform(20,40))
	Winspeed_Fake_Value = int(random.uniform(0,200))
	Sensor_data = {}
	Sensor_data['Hum'] = Humidity_Fake_Value
	Sensor_data['Tem'] = Temperature_Fake_Value
	Sensor_data['Winspeed']= Winspeed_Fake_Value
	Sensor_json_data = json.dumps(Sensor_data)
	publish_To_Topic (MQTT_Topic, Sensor_json_data)
	sleep(1)
	
#================================================
