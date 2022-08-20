import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="*Himgos13")
cursor = mydb.cursor()

cursor.execute("select * from himanshu.ineuron1")
for i in cursor.fetchall():
    print(i)


"""
To check the COMPLETE data/table within database...
cursor.execute("select * from dbname.tablename")
for i in cursor.fetchall():
    print(i)
"""

# TODO: Now if I want to just check the particular column, let say employeeID and email from ineuron1 table..

cursor.execute("select employee_id, emp_mail from himanshu.ineuron1")
for i in cursor.fetchall():
    print(i)

"""
I specified what values I want in...
cursor.execute("select colname, colname from dbname.tablename")
Then fetch value using as they are iterable
"""


# Now to put the data in the list...
cursor.execute("select employee_id, emp_mail from himanshu.ineuron1")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)

# cursor.execute() didn't worked in list function , my observation says it works only one time if iterated earlier.
