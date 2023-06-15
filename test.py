#Python Program to input data to mysql database
#(c) Sai Shibu
#Import pymysql module library

import PyMySQL

#Create a connection to MySQL Database 
conn =pymysql.connect(database="Weatherdata",user="user",password="Pass",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary containing the fields, name, age and place
data={'id':'1','location':kerala,'temperature':'20','humidity':'30'}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO <atmosphere>(id, location, temperature,humidity)VALUES(%(id)s,%(location)s,%(temperature)s),%(humidity)s;",data)
#Close the cursor
cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()

#Open phpMyAdmin and see how the data is stored to the database
