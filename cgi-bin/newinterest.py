#!/usr/bin/python3                                                                                                                                             
import cgi, mysql.connector

form = cgi.FieldStorage()

cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')
cursor = cnx.cursor()

company_id = form.getvalue("company")
interest = form.getvalue("interest")
query = ("UPDATE company SET interest = %s  WHERE company_id = %s")
data = (interest,str(company_id))
cursor.execute(query,data)
cnx.commit()

queryTwo = ("SELECT * FROM company WHERE company_id=%s")
dataTwo = (company_id,)
cursor.execute(queryTwo,dataTwo)

table = cursor.fetchall()
columnNames = ["Company Id", "Company Name", "Address", "COmpany Offer", "Company Debt", "Phone Number", "Interest", "Notes"]
#print ("Content-type:text/html\r\n\r\n")
#print ('<html>')
#print ('<head>')
#print ('<title>Hello Word - First CGI Program</title>')
#print ('</head>')
#print ('<body>')
#print ('<table>')
#print('<tr>')                                                                                                                                                      for i in range(len(columnNames)):
#    print('<th> ' + columnNames[i] + '</th>')
#print('</tr>')                                                                                                                                                     for row in table:
 #   print('<tr>')
  #  print('<td>' + str(row[0]) + '</td>')
   # print('<td>' + row[1] + '</td>')
   # print('<td>' + row[2] + '</td>')
    #print('<td>' + str(row[3]) + '</td>')
    #print('<td>' + str(row[4]) + '</td>')
    #print('<td>' + row[5] + '</td>')
    #print('<td>' + row[6] + '</td>')
    #print('<td>' + row[7] + '</td>')
    #print('</tr>')
#print('</table>')
#print ('</body>')

#print ('</html>')

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print('<table>')
print('<tr>')
for col in columnNames:
    print('<th>' + col + '</th>')
print('</tr>')
for atr in table:
    print('<tr>')
    for i in atr:
        print('<td>' + str(i) + '</td>')
    print('</tr>')
print('<table>')
print ('</body>')
print ('</html>')
cnx.close()
