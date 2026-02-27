'''JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.'''\

#Convert from JSON to Python:

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)                                          #json->py: loads
print(y["age"]) #30


#Convert from Python to JSON
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)                                          #py->json: dumps
# the result is a JSON string:
print(y)    #{"name": "John", "age": 30, "city": "New York"}

#ex
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))                              


#Format the Result
#With indent, JSON is formatted with spaces and new lines.
import json
data = {"name": "Adiya", "age": 16, "city": "Almaty"}
result = json.dumps(data, indent=4)
print(result)
'''indent=4 mean 
-Add a new line for each level
-Add 4 spaces for each indentation level. output:
{
    "name": "Adiya",
    "age": 16,
    "city": "Almaty"
}'''
#You can also define the separators
json.dumps(x, indent=4, separators=(". ", " == "))      #separators = (item_separator, key_separator)
'''{
 "name" == "Adiya". 
 "age" == 16. 
 "city" == "Almaty"
}'''                 
#sort_keys=True → sort keys alphabetically
json.dumps(data, indent=4, sort_keys=True)




