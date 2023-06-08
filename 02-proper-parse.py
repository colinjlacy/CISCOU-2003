
import json

# first we'll read the file
f = open("./data/json-example.json", "r")
data = f.read()

# THEN we'll parse it
parsed = json.loads(data)

# then we'll do something with it!
print(parsed["name"])
