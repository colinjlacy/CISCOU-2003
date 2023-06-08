
# first we'll read the file
f = open("./data/json-example.json", "r")
data = f.read()

# then we'll do something with it!
print(data["name"])
