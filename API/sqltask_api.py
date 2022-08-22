from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host="localhost", user="root", passwd="*Himgos13")
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS tasksql")
cursor.execute("CREATE TABLE IF NOT EXISTS tasksql.tasktable(name varchar(30), number int)")


# Function to insert record in table
@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("INSERT INTO tasksql.tasktable VALUES(%s, %s)",(name, number))
        mydb.commit()
        return jsonify(str('Successfully Inserted'))


# Function to update record
@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("UPDATE tasksql.tasktable SET number = number + 750 WHERE name = %s",(get_name,))   #Always poss tuple
        mydb.commit()
        return jsonify(str('Successfully Updated'))


# Function to delete record
@app.route('/del', methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("DELETE FROM tasksql.tasktable WHERE name = %s",(name_del,))
        mydb.commit()
        return jsonify(str("Successfully Deleted"))


# Function to fetch a data
@app.route('/fetch', methods=['POST'])
def fetch():
    cursor.execute("SELECT * FROM tasksql.tasktable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))


if __name__ == '__main__':
    app.run(port=5003)