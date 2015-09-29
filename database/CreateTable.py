__author__ = 'ugunipati'


import mysql.connector

#Creating a connection
connection = mysql.connector.connect(host = "127.0.0.1",user="root",password="password",database="pqperfaf")
#Creating a cursor using database connection
cursor = connection.cursor()
# SQL Query to create a table
sql= """CREATE TABLE EMPLOYEE (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT )"""
#Execute SQL
cursor.execute(sql)

# Close Connection
connection.close()

