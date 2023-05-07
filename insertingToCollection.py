from pymongo import MongoClient
from datetime import datetime
import os

userpass = os.environ.get('MONGODB_PASS')

MONGODB_URI = f'mongodb+srv://admin:{userpass}@cluster0.jimhqwh.mongodb.net/?retryWrites=true&w=majority'

# Connect to mongoDB cluster 
client = MongoClient(MONGODB_URI)

# Get reference to database
db = client.holiday

# Get collection from database
destination_collection = db.destinations

new_destination = { "country": "Cuba", "date" : datetime(2017,11,28)}

# Write record to collection
result = destination_collection.insert_one(new_destination)

document_id = result.inserted_id
print(document_id)


# Write multiple records to db
new_destinations = [{ "country": "Costa Rica", "date" : datetime(2018,8,23)}, 
                    { "country": "Austria", "date" : datetime(2018,3,4)}]

results = destination_collection.insert_many(new_destinations)
document_ids = results.inserted_ids
print(f'Number of records added: {str(len(document_ids))}')
print(f'_ids inserted are: {document_ids}')

client.close()