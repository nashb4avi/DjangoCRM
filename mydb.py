#Install mysql on computer
#https://dev.mysql.com/downloads/installer
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '123456',

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmcompany")
print("ALL DONE!")
