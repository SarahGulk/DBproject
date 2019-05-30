#!/usr/bin/python3

import cgi, mysql.connector

form = cgi.FieldStorage()

cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')
cursor = cnx.cursor()


companyid = form.getvalue("id")
name = form.getvalue("name")
address = form.getvalue("address")
debt = form.getvalue("debt")
offer = form.getvalue("offer")
phone = form.getvalue("number")
interest = form.getvalue("interest")
note = form.getvalue("note")

query = ("INSERT INTO company (company_id, company_name, company_address, debt_amount, debt_offer, phone_number, interest, notes)"
         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
data= (companyid,name,address,debt,offer,phone,interest,note)
cursor.execute(query,data)
cnx.commit()

#cursor.close()
cnx.close()

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')                                                                                                                                            
print ('<h2>The Company was Inserted</h2>')
print ('</body>')                                                                                                                                           
print ('</html>')
                   
