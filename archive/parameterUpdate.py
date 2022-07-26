import json

file = open("parameters.json", "r")
store = json.loads(file.read())
file.close()


print(store)
paramObj = store["parameters"]