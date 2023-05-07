from pymongo import MongoClient
import pprint
from datetime import datetime
import os

userpass = os.environ.get('MONGODB_PASS')

MONGODB_URI = f'mongodb+srv://admin:{userpass}@cluster0.jimhqwh.mongodb.net/?retryWrites=true&w=majority'

# Connect to mongoDB cluster 
client = MongoClient(MONGODB_URI)

# Get reference to database
db = client.holiday

# Get collection
collection = db.destinations

search = { "country" : { "$in" : ["Cuba", "Germany"] } }
update = { "$set": { "Money Spent" : 1000 } }

result = collection.update_many(search, update)
print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(collection.find_one(search))

client.close()