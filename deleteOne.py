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
document_to_delete = {"country": "Austria"}

# Search for document before delete
print("Searching for target document before delete: ")
pprint.pprint(collection.find_one(document_to_delete))

# Write an expression that deletes the target account.
result = collection.delete_one(document_to_delete)

# Search for document after delete
print("Searching for target document after delete: ")
pprint.pprint(collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()