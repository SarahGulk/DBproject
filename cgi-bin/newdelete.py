#!/usr/bin/python3 
import cgi, mysql.connector

form = cgi.FieldStorage()

cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')
cursor = cnx.cursor()

company_id = form.getvalue("company")
query = ("DELETE FROM company WHERE company_id = %s")
data = (company_id,)
cursor.execute(query, data)
cnx.commit()

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>The company has been deleted</h2>')
print('</form>')
print ('</body>')

print ('</html>')
cnx.close()
