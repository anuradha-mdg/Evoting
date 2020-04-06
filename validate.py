#!C:/python/python.exe
import pymysql
import cgi, os
import cgitb; cgitb.enable()
# Open database connection
db = pymysql.connect("localhost","root","","election")
cursor = db.cursor()
#print ("Content-type:text/html\r\n\r\n")
form = cgi.FieldStorage() 
email=form.getvalue('email')
password=form.getvalue('password')
#email='anuradha@gwintech.com'
#password='as'
sql = "SELECT * FROM users where email = '"+ email + "' and password = '" + password+"'"
#print(sql)
flag=False;
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   #results = cursor.fetchone()
   while True:
        row = cursor.fetchone()
        if row == None:
            break
        flag=True
   db.close()
except pymysql.InternalError as error:
        message = error.args
        print(message)
if flag:
        print("Content-type:text/html\r\nLocation: vote.html\r\n\r\n")    
else :
	print("Content-type:text/html\r\nLocation: login.html?m=1\r\n\r\n")