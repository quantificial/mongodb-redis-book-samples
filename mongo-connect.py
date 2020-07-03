
from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost:27017/test')

print ("test123")

database = client.test

collection = database.books
rows = collection.find({})
for row in rows:
    print(row)

print ("test")