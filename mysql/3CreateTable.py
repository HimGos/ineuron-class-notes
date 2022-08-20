import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="*Himgos13")
cursor = mydb.cursor()


# To create table, first we define the structure of the table i.e. columns
# We define column names to store the data.

s = "create table himanshu.ineuron1(employee_id int(10) , emp_name varchar(80) , emp_mail varchar(20) , emp_salary int(6) , emp_attendance int(3))"
q1 = cursor.execute(s)

"""
Our command to create a table is... 
cursor.execute("create table DATABASENAME.TABLENAME(col1 col1's_data_type(limit) , 
col2 varchar(means string in sql) , ....)")

"""

