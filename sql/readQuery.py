def read_sql_query(sql_query):
  import sqlite3
  import os
  if not os.path.exists("retail.db"):
     from sql.createDB import createDB
     createDB()
     return (None,None)
  try:
      connection = sqlite3.connect("retail.db")
      cursor = connection.cursor()
      cursor.execute(sql_query)
      rows = cursor.fetchall()
      columns = [desc[0] for desc in cursor.description]
      connection.close()
      if len(rows) == 0 :
         return [],[]
      return columns,rows
  except Exception as e:
      return [],[f"Error while querying :{e}"]
  

      
# read_sql_query("SELECT P.TITLE, SUM(O.TOTAL_QUANTITY) AS TOTAL_SOLD FROM ORDERS O JOIN PRODUCTS P ON O.PRODUCT_ID = P.PRODUCT_ID GROUP BY P.TITLE;")