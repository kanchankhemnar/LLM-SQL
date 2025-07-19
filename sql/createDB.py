# create db if doesn't exist
import os
import sqlite3
def createDB():
  # connecting sqlite
  connection = sqlite3.connect("retail.db")

  # creating a cursor object to perform crud operations on db
  cursor = connection.cursor()

  # drop table if it already exists
  cursor.execute("DROP TABLE IF EXISTS CUSTOMERS")
  cursor.execute("DROP TABLE IF EXISTS ORDERS")
  cursor.execute("DROP TABLE IF EXISTS PRODUCTS")


  # Create new table

  cursor.execute(
    '''CREATE TABLE CUSTOMERS(
      CUST_ID INT PRIMARY KEY,
      NAME TEXT,
      ADDRESS TEXT,
      PHONE BIGINT,
      EMAIL TEXT,
      CREATED_AT TIMESTAMP
    )'''
  )

  cursor.execute(
    '''CREATE TABLE PRODUCTS(
      PRODUCT_ID INT PRIMARY KEY,
      TITLE TEXT,
      CATEGORY TEXT,
      CREATED_AT TIMESTAMP,
      DISCOUNT_PER_ITEM INT,
      PRICE_PER_ITEM INT,
      QUANTITY_AVAILABLE INT
    )'''
  )

  cursor.execute(
    '''CREATE TABLE ORDERS(
      ORDER_ID INT PRIMARY KEY,
      CREATED_AT TIMESTAMP,
      CUST_ID INT,
      PRODUCT_ID INT,
      TOTAL_QUANTITY INT,
      TOTAL_DISCOUNT INT,
      TOTAL_PRICE INT,
      DELIVERY_ON TIMESTAMP
    )'''
  )

  # Insert into CUSTOMERS
  cursor.executemany("""
    INSERT INTO CUSTOMERS VALUES (?, ?, ?, ?, ?, ?)
  """, [
    (1, 'Kanchan', 'Pune', 9876543210, 'kanchan@gmail.com', '2023-01-10'),
    (2, 'Apeksha', 'Mumbai', 9876501234, 'apeksha@gmail.com', '2023-02-15'),
    (3, 'Bhavyam', 'Delhi', 9876512345, 'bhavyam@gmail.com', '2023-03-20'),
    (4, 'Kiran', 'Bangalore', 9876523456, 'kiran@gmail.com', '2023-04-05'),
    (5, 'Smit', 'Noida', 7452136896, 'smit@gmail.com', '2023-04-05')
  ])

  # Insert into PRODUCTS
  cursor.executemany("""
    INSERT INTO PRODUCTS VALUES (?, ?, ?, ?, ?, ?, ?)
  """, [
    (101, 'Laptop', 'Electronics', '2023-01-01', 1000, 50000, 10),
    (102, 'Phone', 'Electronics', '2023-01-02', 500, 25000, 20),
    (103, 'Shoes', 'Fashion', '2023-02-01', 200, 3000, 50),
    (104, 'Notebook', 'Stationery', '2023-03-01', 20, 100, 200)
  ])

  # Insert into ORDERS
  cursor.executemany("""
    INSERT INTO ORDERS VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  """, [
    (1001, '2024-01-10', 1, 101, 1, 1000, 49000, '2024-01-15'),
    (1002, '2024-01-15', 1, 102, 2, 1000, 49000, '2024-01-20'),
    (1003, '2024-02-01', 2, 103, 3, 600, 8400, '2024-02-05'),
    (1004, '2024-03-10', 3, 104, 10, 200, 9800, '2024-03-15'),
    (1005, '2024-03-15', 4, 101, 1, 1000, 49000, '2024-03-20'),
    (1006, '2024-04-01', 2, 104, 5, 100, 4900, '2024-04-05')
  ])

  # display the records
  print("Printing records")
  data = cursor.execute('''SELECT * FROM CUSTOMERS ''')
  for row in data:
    print(row)
  
  data = cursor.execute('''SELECT * FROM PRODUCTS ''')
  for row in data:
    print(row)

  data = cursor.execute('''SELECT * FROM ORDERS ''')
  for row in data:
    print(row)
  # close connection once done
  connection.commit()
  connection.close()

if not os.path.exists("retail.db"):
  createDB()
else:
  print("DB already exists")
