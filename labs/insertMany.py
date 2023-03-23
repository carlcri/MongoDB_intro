import os

from pymongo import MongoClient
from dotenv import load_dotenv

# Load config from .env file
load_dotenv()
MONGO_URI = os.environ["MONGO_URI"]

client = MongoClient(MONGO_URI)

db = client.platzi_store
monthlyBudget_collection =db.monthlyBudget

new_documents = [{
    "category": "plants",
    "budget": 100,
    "spent": 230,
},{ "category": "dental care",
    "budget": 301,
    "spent": 400,
    }
]

# Inserting documents 
result = db.monthlyBudget.insert_many(new_documents)

document_ids = result.inserted_ids
print(f'number of docs inserted: {len(document_ids)}')
print(f'document ids: {document_ids}')
print(type(result))
print(type(document_ids))


#print('id of inserted document {document_id}'.format(document_id=document_ids))

client.close()