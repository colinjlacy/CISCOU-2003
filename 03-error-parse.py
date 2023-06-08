
# first we'll read the file
import json

f = open("./data/json-error.json", "r")
data = f.read()

# THEN we'll parse it
parsed = json.loads(data)

# then we'll do something with it!
print(parsed["name"])
