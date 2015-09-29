__author__ = 'ugunipati'

import mysql.connector

cnx=mysql.connector.connect(host = "127.0.0.1",user="root",password="password",database="pqperfaf")
cursor = cnx.cursor()
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    cnx.commit()
    print 'The database insertion completed'
except:
    print 'Not able to insert the '
    cnx.rollback()

cursor.close()