import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)

d = '{"first_name": "Guido","titles": ["BDFL", "Developer"]}'

parsed_json1 = json.loads(d)

print(parsed_json1["BDFL"])
print (parsed_json["first_name"])
print (parsed_json["last_name"])


