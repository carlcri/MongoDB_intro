from pymongo import MongoClient

MONGO_URI = "mongodb+srv://ccrispin:3mB2cAx0D7FNbmiS@cluster0.yddedjv.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)


for db_name in client.list_database_names():
    print(db_name)

client.close()
