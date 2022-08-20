import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="*Himgos13")
cursor = mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())

# cursor.execute("create database mypractice")
# cursor.execute("show databases")
# print(cursor.fetchall())

cursor.execute("create table mypractice.cars2(brand varchar(80) , model varchar(10), engine varchar(10), price_in_usd int(10) )")

cursor.execute("insert into mypractice.cars2 values('Bugatti', 'Chiron', 'v12', 2000000)")
cursor.execute("insert into mypractice.cars2 values('McLaren', 'P1', 'v12', 15000000)")
cursor.execute("insert into mypractice.cars2 values('Lamborghini', 'Huracan', 'v12', 18000000)")

mydb.commit()

cursor.execute("select * from mypractice.cars2")
for i in cursor.fetchall():
    print(i)


# Observation -> error when executed program twice while create database query already executed earlier.
# brand varchar(10) had value 10 and Lamborghini couldn't fit inside so it threw error.
# Since i got error in varchar value, It threw error when I execute again becoz table name CAR already exist.
# It goes on and I reached to car2.

# TODO: Keep values of datatypes during insertion, high. Can save from unexpected long insertion.
