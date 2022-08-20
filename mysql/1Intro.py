# TODO: SQL system always try to store a data in structured format i.e. tables. So to store data sets we create tables

import mysql.connector as conn

# 1. establish communication b\w python and sql.
# Host = where my sql is. Default user is root. Passwd is ur sql pswd

mydb = conn.connect(host="localhost", user="root", passwd = '*Himgos13')
# Once your DB is available in cloud, you are going to do EXACT thing. Just host, user and psw changes

print(mydb)
# if everything is fine, I will get print.

# Table holds the actual data and database is just a folder with multiple files.
# TODO: First we create database then make tables within it.

# 2. To get same query which we are getting in mysql workbench. For that we set a CURSOR.
cursor = mydb.cursor()                     #cursor is like a pointer

# 3. Then we execute our code, just like we did in mysql workbench.
cursor.execute("show databases")

# 4. Fetching details of all databases we received in step 3
print(cursor.fetchall())


# TODO: These 4 lines of code, everytime I have to write!!
"""
1. Establish Connection
2. Set a cursor
3. Execute the code
4. Fetch details
"""

