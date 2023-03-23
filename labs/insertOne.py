import os

from pymongo import MongoClient
from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
MONGO_URI = os.environ["MONGO_URI"]

client = MongoClient(MONGO_URI)

db = client.platzi_store
monthlyBudget_collection =db.monthlyBudget

new_document = {
    "category": "books",
    "budget": 56,
    "spent": 51,
}

# Inserting document 
result = db.monthlyBudget.insert_one(new_document)

document_id = result.inserted_id
print('id of inserted document {document_id}'.format(document_id=document_id))

client.close()