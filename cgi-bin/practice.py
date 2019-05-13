
import mysql.connector

cnx = mysql.connector.connect(user='sgulkowi', database='sgulkowi', password='Esterrachel1')
cursor = cnx.cursor()


def trying(part_id):
  
  query = ("SELECT subpart_id,cost  from part p, subpart s where p.part_id = s.subpart_id")

  cursor.execute(query)

  #find all subparts which reference the part_id given
  #multiply the costs by the amounts
  #sum all the final costs
  #add the final cost
  #return new
  for row in cursor:

    #total = row[2] * row[4]
#base case which is if no subparts
#
    print(row)

    cursor.close()
    cnx.close()

trying("P-100")
