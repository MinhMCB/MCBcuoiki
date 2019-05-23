import pymysql
import json
from datetime import datetime

def Sensor(jsonData):

	json_Dict = json.loads(jsonData)
	Winspeed = json_Dict['Winspeed']
	Data_and_Time = (datetime.today()).strftime("%d-%b-%y %H:%M:%S")
	Temperature = json_Dict['Tem']
	Humidity = json_Dict['Hum']
	n= Temperature
	if n <=30:
		Wstatus = "good"
	else:
		if n<= 35:
			Wstatus= "normal"
		else:
			Wstatus ="bad"
	db= pymysql.connect('localhost','thanhminh','minh6464','mcb2019')
	cursor= db.cursor()

	sql= """insert into Sensor1(Time, Tem, Hum, Winspeed, Wstatus)
			values(%s,%s, %s, %s, %s)
		"""
	val = (Data_and_Time, Temperature, Humidity, Winspeed, Wstatus)
	cursor.execute(sql, val)
	db.commit()

	print("		=>******tao gia tri cam bien moi thanh cong*******")
	print("")
	db.close()

