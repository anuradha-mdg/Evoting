#!C:/python/python.exe
import pymysql
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage() 
# Open database connection
db = pymysql.connect("localhost","root","","election" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
#print ("Content-type:text/html\r\n\r\n")
username=form.getvalue('username')
email=form.getvalue('email')
password=form.getvalue('password')
age=form.getvalue('age')
gender=form.getvalue('gender')
address= form.getvalue('address')
constituency = form.getvalue('cons')
sqlins = "insert into users(username,email,password,age,gender,address,constituency) values(%s,%s,%s,%s,%s,%s,%s)"
sql = "SELECT * FROM users where email = '"+ email + "'"
#print(sql)
flag=False;
try:
      cursor.execute(sql)
      while True:
        row = cursor.fetchone()
        if row == None:
            break
        flag=True
except pymysql.InternalError as error:
        message = error.args
        print(message)

if flag:
    print("Content-type:text/html\r\nLocation: register.html?m=1\r\n\r\n")    
else:
    cursor.execute(sqlins,(username,email,password,age,gender,address,constituency))
    db.commit()  
    print("Content-type:text/html\r\nLocation: regsuccess.html\r\n\r\n")
