claim email sign file
#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('claim'):
   claim_flag = "ON"
else:
   claim_flag = "OFF"

if form.getvalue('email'):
   email_flag = "ON"
else:
   email_flag = "OFF"

if form.getvalue('sign'):
   sign_flag = "ON"
else:
   sign_flag = "OFF"

if files.getvalue('files'):
   files_flag = "ON"
else:
   files_flag = "OFF"

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Checkbox - Third CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> CheckBox Claim is : %s</h2>" % claim_flag
print "<h2> CheckBox Form is : %s</h2>" % sign_flag
print "</body>"
print "</html>"
