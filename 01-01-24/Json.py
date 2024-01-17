import json

# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["city"])




# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)


# # You can convert Python objects of the following types, into JSON strings:

# # dict
# # list
# # tuple
# # string
# # int
# # float
# # True
# # False
# # None

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # print(json.dumps(x))

# print(json.dumps(x, indent=4, separators=("! ", " ? ")))


my_data = {
    "Personal":[
      {
        "name" :  "Nikhil",
        "age" : 23,
        "city" : "Tumakuru"
    }
 ]
}

#  (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.
# json extension type
with open("data_file.json", "w") as write_file:
    json.dump(my_data, write_file)

print(write_file)
print(type(write_file))

#string
json_str = json.dumps(my_data)
print(json_str)
print(type(json_str))

print(json.dumps(my_data, indent=4))