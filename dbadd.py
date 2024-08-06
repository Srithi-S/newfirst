import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='mydatabase')
cur=con.cursor()
cur.execute('ALTER TABLE customer ADD COLUMN country VARCHAR(100)')