import pymongo
import env
import os

MONGODB_URI = os.getenv('MONGO_URI', "Env value not loaded")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find({'first': 'douglas'})

for doc in documents:
    print(doc)