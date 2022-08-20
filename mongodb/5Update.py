import pymongo

client = pymongo.MongoClient("mongodb+srv://himgos13:Himgos13@ineuron.j80ucgd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['inventory']
collection = database['table']

# Where item = canvas , i will update it
# up = collection.update_one({'item': 'canvas'}, {'$set': {'item': 'Himanshu'}})
#
# rec = collection.find({"item":'Himanshu'})
#


# DELETING NOW
collection.delete_one({'item': 'Himanshu'})
rec = collection.find()
for i in rec:
    print(i)

