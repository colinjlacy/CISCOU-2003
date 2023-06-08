import pymongo
import json

# we'll create a database client
client = pymongo.MongoClient("localhost", 27017)
db = client.local
# and then we'll read our example JSON file
f = open("./data/json-example.json", "r")
data = f.read()
# then we'll parse it into a dict
parsed = json.loads(data)
# and insert into a Collection called "clus"
record_id = db.clus.insert_one(parsed).inserted_id

print(record_id)
