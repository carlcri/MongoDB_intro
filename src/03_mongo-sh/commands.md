

sudo docker compose exec mongodb bash

mongosh "mongodb://root:root123@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

show dbs    
use("platzi_store")

show collections
db.products.find()