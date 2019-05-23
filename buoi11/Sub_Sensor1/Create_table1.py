#them thu vien
import MySQLdb
#mo ket noi den Mysql
db= MySQLdb.connect('localhost','thanhminh','minh6464','mcb2019')

# su dung 1 cursor de truy cap
cursor= db.cursor()

# xoa table neu table da ton tai
cursor.execute("drop table if exists Sensor1")

# tao 1 bang
sql= """ create table Sensor1(
			ID int(5) not null auto_increment primary key,
			Tem float(3) not null,
			Hum float(3) not null,
			Winspeed float(3) not null,
			Wstatus char(25) not null,
			Time char(25) not null
		)"""
# thuc thi
cursor.execute(sql)
db.close()
