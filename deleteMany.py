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

# Filter by ObjectId
document_to_delete = {"Money Spent": { "$lt" :  2000 } }

# Search for document before delete
print("Searching for target document before delete: ")
cursor = collection.find(document_to_delete)
for document in cursor:
    pprint.pprint(document)

# Write an expression that deletes the target account.
result = collection.delete_many(document_to_delete)

# Search for document after delete
print("Searching for target document after delete: ")
pprint.pprint(collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()