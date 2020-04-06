#!C:/python/python.exe
print ("Content-type:text/html\r\n\r\n")
import pymysql
import cgi, os
# Open database connection
db = pymysql.connect("localhost","root","","election" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = "SELECT * FROM results"
print(""" <!DOCTYPE html>
<html lang="en">
<head>
    <title>Home</title>
    <meta charset="utf-8">
	  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Your description">
    <meta name="keywords" content="Your keywords">
    <meta name="author" content="Your name">
    <link rel="icon" href="images/favicon.ico" type="image/x-icon">
    <link rel="shortcut icon" href="images/favicon.ico" type="image/x-icon" />
    <link rel="stylesheet" href="css/bootstrap.css" type="text/css" media="screen">
    <link rel="stylesheet" href="css/responsive.css" type="text/css" media="screen">
    <link rel="stylesheet" href="css/camera.css" type="text/css" media="screen"> 
    <link rel="stylesheet" href="css/style.css" type="text/css" media="screen">
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,600,700' rel='stylesheet' type='text/css'>
  	<script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/jquery.easing.1.3.js"></script>
  	<script type="text/javascript" src="js/camera.js"></script>
    <script src="js/jquery.ui.totop.js" type="text/javascript"></script>
    
  	<script>
        $(document).ready(function(){   
                jQuery('.camera_wrap').camera();
          });    
  	</script>
    <script type="text/javascript" src="js/jquery.mobile.customized.min.js"></script>
	
	<style>
table {
    border-collapse: collapse;
	
}

table, td, th {
     border: 1px solid LightGray;
}
td
{padding:30px;font-size:20px;}
.center {
    margin: auto;
    width: 60%;
   
    padding: 10px;
}
th
{padding:25px;font-size:20px;}
</style>
</head>

<body>
<!--==============================Header=================================-->
<header>
    <div class="container">
    	<div class="row">
        	<div class="span12">
            	<div class="clearfix">
                    <div class="clearfix header-block-pad">
                        <h1 class="brand"><a href="index.html"></a><span>Online Voting System</span></h1>
                    </div>
              </div>
           </div>
      </div>   
    </div>
    
    <!--==============================Nav=================================-->          
    <div id="nav_section">
      <div class="container">
        <div class="row">
          <div class="span12">
            <div class="navbar navbar_ clearfix">
              <div class="navbar-inner navbar-inner_">
                  <div class="container">
                      <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse_">MENU</a>                                                   
                      <div class="nav-collapse nav-collapse_ collapse">
                          <ul class="nav sf-menu">
                            <li class="active li-first"><a href="index.html">Home</a></li>
                            <li class="sub-menu"><a href="about.html">about</a>
                              
                            </li>
                            <li><a href="login.html">Login</a></li>
                            <li><a href="results.py">Results</a></li>
                            
                          </ul>
                      </div>
                      
                  </div>
              </div>
            </div>
          </div>
        </div>   
      </div>
    </div>
    <!--==============================End Nav=================================-->

    <!--==============================Slider=================================--> 
    <div class="slider">
    <div class="camera_wrap">
        <div data-src="images/slide1.jpg"></div>
        <div data-src="images/slide2.jpg"></div>
        <div data-src="images/slide4.jpg"></div>
       
    </div>
</div>
</header>

<!--==============================Content=================================--> 
<section id="content" class="main-content">
  <div class="container">
  <div class="center">
"""	)
print("<table><tr><th>SL.No</th><th>Party Name</th><th>Vote Count</th></tr>")
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      party_id = row[0]
      party_name = row[1]
      result = row[2]
	  
      # Now print fetched result
      print("<tr><td>"+ str(party_id)+"</td><td> " +party_name+ "</td><td>"+str(result)+"</td></tr>")

except:
   print("Error: unable to fecth data")
# disconnect from server
db.close()  
print("</table>")
print(""" </div>
</section>
<footer>
   <div class="container">
    <div class="row">
      <div class="span12">ONLINE VOTING SYSTEM 2018. ALL RIGHTS RESERVED.</div>
    </div>
   </div>
</footer>
<script type="text/javascript" src="js/bootstrap.js"></script>
</body>
</html> """)
