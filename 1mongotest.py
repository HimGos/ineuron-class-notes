import pymongo

client = pymongo.MongoClient("mongodb+srv://himz:Himgos13@cluster0.n3cfr42.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name': 'Himanshu',
    'email': 'himgos@gmail.com',
    'surname': 'goswami'
}

e = {
    'name': 'Himanshu',
    'email': 'himgos@gmail.com',
    'surname': 'goswami'
}

f = {
   'name': 'Himanshu',
    'email': 'himgos@gmail.com',
    'surname': 'goswami'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_many([d,e,f])