#1.create database demo
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306)
cur=con.cursor()
cur.execute('CREATE DATABASE demo')
#9.first row
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT * from person')
res=cur.fetchone()
print(res)
#4.multiple value
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
sql="INSERT INTO person(name,email,contact,address,country)VALUES(%s,%s,%s,%s,%s)"
val=('annu','ann@gmail.com','987654324','annu villa north','India')
cur.execute(sql,val)
con.commit()
#8.select email and country from table
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT email,country from person')
res=cur.fetchall()
for i in res:
    print(i)
#11.select in ASC based on name
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT * from person ORDER BY name ASC')
res=cur.fetchall()
for i in res:
    print(i)
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('DELETE FROM person  WHERE person_id=7')
con.commit()
#12 select in desc
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT * from person ORDER BY name DESC')
res=cur.fetchall()
for i in res:
    print(i)
#7.avoid duplicate value
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT DISTINCT name,email,contact,address,country  from person')
res=cur.fetchall()
for i in res:
    print(i)
#10.select id=6
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT * from person WHERE person_id=6')
res=cur.fetchall()
for i in res:
    print(i)
#3.insert a single value to thae table person
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
sql="INSERT INTO person(name,email,contact,address,country)VALUES(%s,%s,%s,%s,%s)"
val=('annu','ann@gmail.com','987654324','annu villa north','India')
cur.execute(sql,val)
con.commit()
#4.insert multiple values
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
sql="INSERT INTO person(name,email,contact,address,country)VALUES(%s,%s,%s,%s,%s)"
val=[('malu','malu@gmail.com','897654390','malu villa,south','India'),('arya','arya@gmail.com','768909875','arya bhavan,east','India'),('helen','helen@gmail.com','908756432','helen villa','China'),('vennu','vennu@gmail.com','8975644352','vennu villa','japan'),('raju','raju@gmail.com','879435627','raju villa','USA')]
cur.executemany(sql,val)
con.commit()
print(cur.rowcount,'rowinserted')
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT * from person')
print(cur.rowcount,'rowinserted')
#3.value retrieve by pattern
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='srithi',port=3306,database='demo')
cur=con.cursor()
cur.execute('SELECT * from person WHERE country LIKE "j%"')
res=cur.fetchall()
for i in res:
 print(i)