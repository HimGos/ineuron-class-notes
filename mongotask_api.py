from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://himgos13:Himgos13@ineuron.j80ucgd.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
coll = database['taskcollection']


# Inserting in mongodb
@app.route('/minsert', methods= ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        coll.insert_one({name:number})
        return jsonify(str("Successfully inserted"))


# Updating in mongodb
@app.route('/mupdate', methods= ['POST'])
def update():
    if request.method == 'POST':
        name = request.json['name']
        new_num = request.json['new_num']
        coll.update_one({"name":name}, {'$set': {"number": new_num}})
        return jsonify(str("Successfully updated"))


@app.route('/mdelete', methods= ['POST'])
def delete():
    if request.method == 'POST':
        name = request.json['name']
        coll.delete_one({"name":name})
        return jsonify(str("Successfully deleted"))


@app.route('/mfetch', methods= ['POST'])
def fetch():
    l = []
    for i in coll.find():
        l.append(i)
    return jsonify(str(l))


if __name__ == '__main__':
    app.run(port = 5001)       # Changed port becoz previous task was conficting