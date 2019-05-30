#!/usr/bin/python3                                                                                                                                        
import cgi, mysql.connector

form = cgi.FieldStorage()

cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')
cursor = cnx.cursor()

company_id = form.getvalue("company")
new_id = company_id.split("_")[0]
query = ("SELECT * FROM company WHERE company_id=%s")
data = (new_id,)
cursor.execute(query,data)

table = cursor.fetchone()
columnNames = ["Company Id", "Company Name", "Address", "COmpany Offer", "Company Debt", "Phone Number", "Interest", "Notes"]
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print('<table>')
for i in range(len(table)):
    print('<tr> <th> ' + columnNames[i] + '</th> <td> ' +  str(table[i]) + '</td> </tr>')
print('</table>')
print ('<form>')
print ('<input type="button" value="Delete Company" onclick="location.href=\'delete.py?company=' + str(new_id) + '\'">')    
print ('<input type="button" value="Update Interest" onclick="location.href=\'interest.py?company=' + str(new_id) + '\'">')
print ('<input type="button" value="Update Notes" onclick="location.href=\'notes.py?company=' + str(new_id) +' \'">')
print('</form>')
print ('</body>')                                                                                                                                        

print ('</html>')
cnx.close()
