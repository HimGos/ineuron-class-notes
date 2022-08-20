import pymongo

client = pymongo.MongoClient("mongodb+srv://himgos13:Himgos13@ineuron.j80ucgd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database['himz']


# Finding data
# data = collection.find({'course' : 'iNeuron'})
# for i in data:
#     print(i)


# Finding data with condition
data = collection.find({'courses' : {"$gt" : 'E'} })
for i in data:
    print(i)