from bson.json_util import dumps
from pymongo import MongoClient

# we'll create a database client
client = MongoClient("localhost", 27017)
db = client.local
# and we'll query for the document we just inserted
cursor = db.clus.find({"name": "Cisco Systems, Inc."})
as_dict = cursor.next()
# then we'll print it as JSON
print(dumps(as_dict, indent=4))
