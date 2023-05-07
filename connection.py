from pymongo import MongoClient
from datetime import datetime
import os

userpass = os.environ.get('MONGODB_PASS')

MONGODB_URI = f'mongodb+srv://admin:{userpass}@cluster0.jimhqwh.mongodb.net/?retryWrites=true&w=majority'

# Connect to mongoDB cluster 
client = MongoClient(MONGODB_URI)

# List all of the databases in the cluster
for db_name in client.list_database_names():
     print(db_name)

# Get reference to database
db = client.sample_airbnb
print(db.list_collection_names())


client.close()