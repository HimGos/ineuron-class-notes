import mysql.connector as conn

mydb = conn.connect(host='localhost', user='root', passwd='*Himgos13')
cursor = mydb.cursor()

cursor.execute("CREATE DATABASE del_later")
cursor.execute("CREATE TABLE del_later.snydix(company_name varchar(80),"
               "address varchar(250),"
               "employees_no int(250) ) "
               " ")

cursor.execute("INSERT INTO del_later.snydix "
               " VALUES ('Del Monte', 'Connaught Place', 125),"
               "('Rosche Dona', 'San Fransisco, Los Angeles', 75),"
               "('Lemix Iok', 'Sheikh Zayd Road, Dubai', 156)"
               " ")

# TODO : Another way of writing ...
# s = "INSERT INTO del_later.snydix VALUES(%s %s %s)"
# a1 = ('Del Monte', 'Connaught Place', 1252)          # Can take value from user here
# TODO: cursor.execute(s,a1)
# big = [('Rosche Dona', 'San Fransisco, Los Angeles', 758), ('Lemix Iok', 'Sheikh Zayd Road, Dubai', 9856)]
# TODO: cursor.executemany(s,big)

mydb.commit()

cursor.execute("UPDATE del_later.snydix SET address = '45 Duxton, Silicon Valley' WHERE employees_no = 125")

mydb.commit()

cursor.execute(" DELETE FROM del_later.snydix WHERE employees_no = 75")
mydb.commit()

cursor.execute("SELECT *"
               "FROM del_later.snydix")

result = cursor.fetchall()
for i in result:
    print(i)