import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="*Himgos13")
cursor = mydb.cursor()

# In this step we create a database named himanshu
cursor.execute("create database himanshu")

"""
cursor.execute() takes the command to perform in mysql
"""

cursor.execute("show databases")
print(cursor.fetchall())


"""
We just added one step where we CREATED database, except that other 4 steps are same!
"""
