import os
import pprint
from pymongo import MongoClient

userpass = os.environ.get('MONGODB_PASS')

MONGODB_URI = f'mongodb+srv://admin:{userpass}@cluster0.jimhqwh.mongodb.net/?retryWrites=true&w=majority'

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Calculate the average balance of checking and savings accounts with balances of less than $1000.

# TODO 1: Select accounts with balances of less than $1000.
select_by_balance = {"$match" : { "balance" : { "$lt" : 1000} }}

# TODO 2: Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = { "$group" : { "_id" : "$account_type", "avg_balance" : { "$avg" : "$balance"} }}

# TODO 3: Create an aggegation pipeline using 'select_by_balance' and 'separate_by_account_calculate_avg_balance'.
pipeline = [select_by_balance,
            separate_by_account_calculate_avg_balance]

# TODO 4: Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print(
    "Average balance of checking and savings accounts with balances of less than $1000:"
)

for item in results:
    pprint.pprint(item)

client.close()
