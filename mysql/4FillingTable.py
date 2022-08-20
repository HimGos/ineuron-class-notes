import mysql.connector as conn

mydb = conn.connect(host= "localhost", user="root", passwd="*Himgos13")
cursor = mydb.cursor()

# We have already created table -> ineuron .. within himanshu database

cursor.execute("insert into himanshu.ineuron1 values(101 , 'himz' , 'himgos@gmail', 550, 30)")


"""
Our command to fill the table ...
cursor.execute("insert into databasename.tablename values(v1 ,v2... same no. of values as per column nos.)")
"""

# TODO: To finalize my data insert, i need to COMMIT ... It's like assuring the data.

mydb.commit()

# DONE!



sqlFormula = "INSERT INTO students (name,age) VALUES (%s, %s)"
student = [('Himz', 26),
            ('Linkon', 29),
            ('Sid', 34)]

cursor.executemany(sqlFormula, student)
mydb.commit()