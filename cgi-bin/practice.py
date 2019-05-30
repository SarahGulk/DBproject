#!/usr/bin/python
import mysql.connector

cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')
cursor = cnx.cursor()
 
#query = ("SELECT * FROM company")

#cursor.execute(query)

  #find all subparts which reference the part_id given
  #multiply the costs by the amounts
  #sum all the final costs
  #add the final cost
  #return new
mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM company")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
