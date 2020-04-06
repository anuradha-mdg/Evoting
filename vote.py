#!C:/python/python.exe
import pymysql
import cgi, os
form = cgi.FieldStorage() 
party=form.getvalue('party')
# Open database connection
db = pymysql.connect("localhost","root","","election" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = " UPDATE results SET result = result + 1 WHERE id = "+party
try:
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print("Content-type:text/html\r\nLocation: success.html\r\n\r\n")
except pymysql.InternalError as error:
        message = error.args
        print(message)
# disconnect from server
db.close()
