import pymongo

client = pymongo.MongoClient("mongodb+srv://himgos13:Himgos13@ineuron.j80ucgd.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['inventory']
collection = database['table']


data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


# collection.insert_many(data)

# rec = collection.find({'status': "A"})

# Finding all status where status is either A or P
# rec = collection.find({'status': {"$in" : ['A', "P"] }})


# Finding status where status greater than C
# rec = collection.find({"status" : {"$gt": "C"}})


# Finding qty grater or equal to 75 and status D
# rec = collection.find({'qty' : {"$gte": 75} , 'status' : 'D'})

# rec = collection.find({'item': 'sketch pad' ,'qty':95})

# In this line we are using AND condition
# rec = collection.find({'item': 'sketch pad', 'qty': {"$gte" : 75}})


# In this line we are using OR condition
# rec = collection.find({"$or" : [{'item' : 'sketch pad'} , {'qty': {'$gte':75}}]})


for i in rec:
    print(i)