#!C:/python/python.exe
import pymysql
import cgi, os
import cgitb; cgitb.enable()
# Open database connection
db = pymysql.connect("localhost","root","","election")
cursor = db.cursor()
#print ("Content-type:text/html\r\n")
form = cgi.FieldStorage() 
email=form.getvalue('email')
#email='anuradha@gwintech.com'
#password='as'
sql = "SELECT * FROM users where email = '"+ email + "'"
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
      print(1)
		
else:
      print(0)	  
