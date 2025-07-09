def read_sql_query(sql_query):
  import sqlite3
  import os
  if not os.path.exists("student.db"):
     from sql.createDB import createDB
     createDB()
  try:
      connection = sqlite3.connect("student.db")
      cursor = connection.cursor()
      cursor.execute(sql_query)
      rows = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      connection.close()
      if len(rows) == 0 :
         return [],[]
      return columns,rows
  except Exception as e:
      return [],[("Error while querying ",e)]
      
