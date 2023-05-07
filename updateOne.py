from pymongo import MongoClient
from datetime import datetime
import pprint
import os

userpass = os.environ.get('MONGODB_PASS')

MONGODB_URI = f'mongodb+srv://admin:{userpass}@cluster0.jimhqwh.mongodb.net/?retryWrites=true&w=majority'

# Connect to mongoDB cluster 
client = MongoClient(MONGODB_URI)

# Get reference to database
db = client.holiday

# Get collection
collection = db.destinations

search = { "country" : "New Zealand"}
update = { "$inc": { "Money Spent" : 150 } }

pprint.pprint(collection.find_one(search))

result = collection.update_one(search, update)
pprint.pprint(collection.find_one(search))


client.close()