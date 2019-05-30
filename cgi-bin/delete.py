#!/usr/bin/python3                                                                                                                                             
import cgi, mysql.connector

form = cgi.FieldStorage()

company_id = form.getvalue('company')

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print('<form action="newdelete.py">')
print ('</h2>Are you sure you would like to delete the company with the following ID?</h2>')
print('<input type="text" name="company" value="'+company_id+'">')
print ('<input type = "submit" value="Delete">')
print('</form>')
print ('</body>')

print ('</html>')
    
