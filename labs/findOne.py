import os, pprint
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId

# Load config from .env file
load_dotenv()
MONGO_URI = os.environ["MONGO_URI"]

client = MongoClient(MONGO_URI)

db = client.platzi_store
monthlyBudget_collection =db.monthlyBudget

# Prints the first element
result = db.monthlyBudget.find_one()
os.system("echo first element with findOne | lolcat")
pprint.pprint(result)


# Querry by ObjectId
document_to_find = {"_id": ObjectId("641bbe734fcb262600072f77")}
result = db.result = db.monthlyBudget.find_one(document_to_find)
os.system("echo querryng by Object Id | lolcat")
pprint.pprint(result)

# Querry by ObjectId with projection
document_to_find = {"_id": ObjectId("641bbe734fcb262600072f77")}
result = db.result = db.monthlyBudget.find_one(document_to_find, {"budget" : 1})
os.system("echo using projections | lolcat")
pprint.pprint(result)

client.close()