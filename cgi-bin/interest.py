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
print('<form action="newinterest.py">')
print('<input type="text" name="company" value="'+company_id+'">')
print ('<input type="text" name="interest">  Update interest Here:')
print ('<input type = "submit" value="Update Interest">')
print('</form>')
print ('</body>')

print ('</html>')
