__author__ = 'ugunipati'

import mysql.connector

cnx=mysql.connector.connect(host = "127.0.0.1",user="root",password="password",database="pqperfaf")
cursor = cnx.cursor()
sql = "(select id, name, description from pqperfaf.perf_runs)"
cursor.execute(sql)
for(id,name,description) in cursor:
    print id
    print name
    print description
cursor.close()
cnx.close()