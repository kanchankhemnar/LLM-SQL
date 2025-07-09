# create db if doesn't exist
import os
import sqlite3
def createDB():
  # connecting sqlite
  connection = sqlite3.connect("student.db")

  # creating a cursor object to perform crud operations on db
  cursor = connection.cursor()

  # drop table if it already exists
  cursor.execute("DROP TABLE IF EXISTS STUDENTS")

  # Create new table
  cursor.execute("""
      CREATE TABLE STUDENTS (
          NAME TEXT,
          CLASS TEXT,
          SECTION TEXT,
          MARKS INT
      )
  """)

  # Insert records
  cursor.execute('''
      INSERT INTO STUDENTS VALUES ("KANCHAN", "IT", "A", 90)
  ''')
  cursor.execute('''
      INSERT INTO STUDENTS VALUES ("APEKSHA", "ENTC", "B", 85)
  ''')
  cursor.execute('''
      INSERT INTO STUDENTS VALUES ("BHAVYAM", "CE", "A", 100)
  ''')
  cursor.execute('''
      INSERT INTO STUDENTS VALUES ("KIRAN", "CE", "A", 90)
  ''')
  cursor.execute('''
      INSERT INTO STUDENTS VALUES ("SMIT", "CE", "B", 50)
  ''')
  # display the records
  print("Printing records")
  data = cursor.execute('''SELECT * FROM STUDENTS''')
  for row in data:
    print(row)
  
  # close connection once done
  connection.commit()
  connection.close()

if not os.path.exists("student.db"):
  createDB()
else:
  print("DB already exists")
