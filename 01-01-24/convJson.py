import json
# Converting dic to JSON 
# my_data = {
#     "Personal":[
#       {
#         "name" :  "Nikhil",
#         "age" : 23,
#         "city" : "Tumakuru"
#     }
#  ]
# }

#  (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.
# json extension type
# with open("data_file.json", "w") as write_file:
#     json.dump(my_data, write_file)

# print(write_file)
# print(type(write_file))

# #string
# json_str = json.dumps(my_data)
# print(json_str)
# print(type(json_str))

# print(json.dumps(my_data, indent=4))

# # Converting list to JSON string

# numbers = [1, 2, 3, 4, 5]

# # Converting list to JSON string
# json_string = json.dumps(numbers)
# print("JSON String (List):", json_string)

# load() and loads() for turning JSON encoded data into Python objects.
# blackjack_hand = (8, "Q")
# encoded_hand = json.dumps(blackjack_hand)
# decoded_hand = json.loads(encoded_hand)

# print(blackjack_hand == decoded_hand)

# print(type(blackjack_hand))

# print(type(decoded_hand))

# print(blackjack_hand == tuple(decoded_hand))



# # JSON string representing a dictionary
# json_data = '{"name": "Alice", "age": 28, "city": "London"}'

# # Decoding JSON string to a Python dictionary
# decoded_dict = json.loads(json_data)
# print("Decoded Dictionary:", decoded_dict)
# print("Type of Decoded Data:", type(decoded_dict))




# # JSON string representing a list
# json_data = '[1, 2, 3, 4, 5]'

# # Decoding JSON string to a Python list
# decoded_list = json.loads(json_data)
# print("Decoded List:", decoded_list)
# print("Type of Decoded Data:", type(decoded_list))




# # JSON string representing a string value
# json_data = '"Hello, world!"'

# # Decoding JSON string to a Python string
# decoded_string = json.loads(json_data)
# print("Decoded String:", decoded_string)
# print("Type of Decoded Data:", type(decoded_string))




# # JSON string representing a numeric value
# json_data = '3.14159'

# # Decoding JSON string to a Python numeric value
# decoded_numeric = json.loads(json_data)
# print("Decoded Numeric Value:", decoded_numeric)
# print("Type of Decoded Data:", type(decoded_numeric))





# # JSON string representing a boolean value
# json_data = 'true'

# # Decoding JSON string to a Python boolean
# decoded_boolean = json.loads(json_data)
# print("Decoded Boolean:", decoded_boolean)
# print("Type of Decoded Data:", type(decoded_boolean))



employee = {
    "ename": 'Raju',
    "age": 25,
    "Designation": 'Jnr Dev',
    "LPA": 5
}

print(type(employee))
print(employee)


# Writing the employee dictionary to a JSON file
with open("data_file.json", "w") as my_emp:
    json.dump(employee, my_emp)
print('Converting...........')
print('Conversion complete!')
print(my_emp)
print(type(my_emp))

# Reading the JSON file and loading its content into another variable
with open("data_file.json", "r") as my_emp:
    emp = json.load(my_emp)

print(type(emp))
print(emp)

print('Extract the required value...')

extract = emp['age']
print(extract)

print('Let\'s append')

new_data = {
    "City" : 'Blr',
    "Hobbies" : 'Swimming, Drinking'
}

emp.update(new_data)
print(emp)




# Load existing JSON data
with open("data_file.json", "r") as emp:
    existing_data = json.load(emp)

print (type(emp))

# New data to append
ne_data = {
    "City": 'Blr',
    "Hobbies": 'Swimming, Drinking'
}

# Appending the new data to the existing data
existing_data.update(ne_data)


# Write the updated data back to the JSON file
with open("data_file.json", "w") as emp:
    json.dump(existing_data, emp, indent=4)  # indent for better readability (optional)

with open("data_file.json", "r") as my_emp:
    emp = json.load(my_emp)
print(type(emp))
print(emp)

