#!/usr/bin/python

import cgi   

form = cgi.FieldStorage()   
#first_name = form.getvalue('first_name')
#last_name  = form.getvalue('last_name')
print "Content-type:text/html\r\n\r\n"
print' <html>'
print '<head>'
print '<title>Page Title</title>'
print '</head>'
print '<body>'

print '<h1>It worked</h1>'
print '<body style="background-color:powderblue;">'
#print '</body>'
#print '<form>'
#print 'First name:<br>'
#print '<input type="text" name="first_name"><br>'
#print 'Last name:<br>'
#print '<input type="text" name="last_name">'
#print '<input type="submit" value="Submit">'
#print '</form>'
#print "<body>"
#print "<h2>Hello %s %s</h2>" % (first_name, last_name)
#print "</body>"
#print '</html>'
print '<form>'
print '<input type="radio" name="status" value="current" checked> Current Case<br>'
print '<input type="radio" name="status" value="new"> New Case<br>'
print '</form>'
print '</html>'
