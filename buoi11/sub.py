import paho.mqtt.client as mqtt
from datetime import *
import MySQLdb

#mo ket noi voi mysql
#db = MySQLdb.connect('localhost','thanhminh','minh6464','wsn')
#cursor=db.cursor()
#===========================
# MQTT settings

MQTT_Broker = "localhost"       # ten may chu
MQTT_Port = 1883                # port mac dinh cua MQTT
Keep_Alive_Interval = 45        # thoi gian gia cac lan gui goi tin
MQTT_Topic = "demo"

#======================================================
# Ham ket noi may chu (thong bao khi ket noi thanh cong)

def on_connect(client, userdata ,flags, rc):
        if rc != 0:	# ket noi thanh cong hi rc khac 0
                pass
                print ( "khong the ket noi MQTT...")
        else:
                print("Ket noi thanh cong  voi MQTT Broker:" + str(MQTT_Broker))
	client.subscribe(MQTT_Topic,0)

#=====================================================
# Gui thong bao khi nhan duoc du lieu publish den topic

def on_message(client, userdata, msg):
	# this is master call for saving mqtt data into db
	# for details of "sensor_data_handler" function please
	# refer "sensor_data_to_db.py
	#print ("MQTT Data Received...")
	#print ("MQTT Topic: " + msg.topic)
	print ("Data: " + str(msg.payload))

#========================================================
client = mqtt.Client()
client.username_pw_set(username="ntm",password="minh6464")       #thay d
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_Broker, MQTT_Port , Keep_Alive_Interval)
client.loop_forever()


