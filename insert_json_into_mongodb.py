import json
from pymongo import MongoClient

# Read the JSON file
with open('formatted_output.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# MongoDB connection setup
CONNECTION_STR = "HEHEHE"
client = MongoClient(CONNECTION_STR)

dbname = 'HEHEHEDB'
clname = 'HEHEHECL'
# Replace with your MongoDB connection string
db = client[dbname]  # Use your database name
collection = db[clname]  # Use your collection name

# Insert each record into the collection
for record in data:
    collection.insert_one(record)

print("Records inserted into the MongoDB collection")
