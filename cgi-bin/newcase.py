#!/usr/bin/python3                                                                                                                                             

import cgi, mysql.connector

form = cgi.FieldStorage()

cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')
cursor = cnx.cursor()


caseid = form.getvalue("id")
companyid= form.getvalue("cid")
name = form.getvalue("name")
date = form.getvalue("date")
percent = form.getvalue("percent")
employee = form.getvalue("employee")
note = form.getvalue("note")

query = ("INSERT INTO CurrentCase (case_number, company_id, case_company, last_date, percentage, employee_id, notes)"
         "VALUES (%s,%s,%s,%s,%s,%s,%s)")
data= (caseid,companyid,name,date,percent,employee,note)
cursor.execute(query,data)
cnx.commit()

#cursor.close()                                                                                                                                               
case = form.getvalue("id")
query = ("SELECT case_number, company_id, case_company, last_date, percentage, employee_id, notes FROM CurrentCase WHERE case_number=%s")
data = (case,)
cursor.execute(query,data)

table = cursor.fetchone()
columnNames = ["Case Id", "Company ID", "Case Company", "Last Date", "Percentage", "Employee",  "Notes"]
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print('</head>')
print('<body>')
print('<table>')
for i in range(len(table)):
    print('<tr> <th> ' + columnNames[i] + '</th> <td> ' +  str(table[i]) + '</td> </tr>')
print('</table>')
print ('</body>')

print ('</html>')
cnx.close()
