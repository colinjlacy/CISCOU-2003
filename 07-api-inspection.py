import requests

resp = requests.get("http://127.0.0.1:5000")

# print("the text property returns a", type(resp.text), resp.text)
print("the json method returns a", type(resp.json()), resp.json())
