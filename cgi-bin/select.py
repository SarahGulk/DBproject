#!/usr/bin/python3


import cgi, mysql.connector
form = cgi.FieldStorage()

def db_dropdown():  # Execute query
    cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')                                                              
    cursor = cnx.cursor()
    sql = ('SELECT company_id, company_name FROM company')
    cursor.execute(sql)
    list_tested = cursor.fetchall()  # Get query response and store in variable
    #list_tested = [i for sub in list_tested for i in sub]  # Convert to list from tuple
    return list_tested

def print_dropdown(data):  # Print the dropdown
    print ('<div>')
    print ('<select name="company">')
    for i in data:
        print ('<option value="%d_%s">%s</option>' % (i[0], i[1],i[1]))
    print ('</select>')
    print ('</div>')


print ("Content-type:text/html\r\n\r\n")                                                                                                                 
print ('<html>')                                                                                                                                         
print ('<head>')                                                                                                                                         
print ('<title>Hello Word - First CGI Program</title>')                                                                                                  
print ('</head>')
print ('<body style="background-color:powderblue;">')
print ('<form action="update.py" method = "get">')
info = db_dropdown()
print_dropdown(info)
print ('<input type="submit" value="Submit">')

print ('</form>')
print ('</body>')                                                                                                                                        
print ('</html>')

