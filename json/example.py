import json

json_data = open("example.json").read()
parsed_data = json.loads(json_data)

print(parsed_data)

