from pymongo import MongoClient
from datetime import datetime
from pprint import pprint
import os

userpass = os.environ.get('MONGODB_PASS')

MONGODB_URI = f'mongodb+srv://admin:{userpass}@cluster0.jimhqwh.mongodb.net/?retryWrites=true&w=majority'

# Connect to mongoDB cluster 
client = MongoClient(MONGODB_URI)

# Get reference to database
db = client.holiday

# Get collection
collection = db.destinations

search = { "country" : { "$in" : ["Indonesia", "Germany"] } }

cursor = collection.find(search)
for document in cursor:
    pprint(document)

client.close()