import json

#Example Json
x = '{"name":"Layson", "age":"25", "city":"Manila"}'

#Parse Json

y = json.loads(x)
print ("the output of the json file is", y)
print ("Name", y["name"], "Age", y["age"], "City", y["city"])