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

cursor = db.monthlyBudget.find({ "budget": {"$gte": 301}},
                               { "_id": 0, "budget": 1})

os.system('echo querrying multiple docs and projections | lolcat ')
for document in cursor:
    pprint.pprint(document)


print(type(cursor))