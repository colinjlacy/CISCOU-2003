
# first we'll read the file
import json

f = open("./data/json-example.json", "r")
data = f.read()
parsed = json.loads(data)

# now we'll edit it
parsed["industry"] = "networking"

# and we'll try to save it
f = open("./data/output.json", "w")
f.write(parsed)
