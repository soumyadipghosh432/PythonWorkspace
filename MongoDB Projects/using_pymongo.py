import pymongo
from pymongo import MongoClient

#  make db connection
connection = MongoClient('localhost',27017)
db = connection.m101
collection = db.hw1
item = collection.find_one()

print(item)
print(item['question'])