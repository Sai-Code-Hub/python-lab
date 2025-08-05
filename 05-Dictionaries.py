# /*Dictionaries
# We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.
#
# This section will serve as a brief introduction to dictionaries and consist of:
#
# 1.) Constructing a Dictionary
# 2.) Accessing objects from a dictionary
# 3.) Nesting Dictionaries
# 4.) Basic Dictionary Methods
# So what are mappings? Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.
#
# A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.
#
# Constructing a Dictionary
# ----------------------->>

# Create a dictionary with keys and values
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Access value using key
print("Access key2:", my_dict['key2'])  # Output: value2
print("Access key1:", my_dict['key1'])  # Output: value1

prices_lookup = {'apple': 2.99,'orange': 4.99,'milk':5.80}
print("Access prices:", prices_lookup)
print("Access prices:", prices_lookup['orange'])

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100,'outsideKey':200 }}
print("Access keys:", d['k1'])
print("Access keys:", d['k3'])

d1 = {'key1':['a','b','c']}
print("Access keys:", d1)
mylist = d1['key1']
print("Access keys:", mylist)
letter = mylist[2]
print("Access letter:", letter)
letter.upper()
print("Access letter:", letter)
# letter.lower()
# print("Access letter:", letter)
print(d1['key1'][2].upper())


# A dictionary with multiple data types
my_dict = {
    'key1': 123,
    'key2': [12, 23, 33],
    'key3': ['item0', 'item1', 'item2']
}

# Access a list stored in key3
print("List under key3:", my_dict['key3'])  # Output: ['item0', 'item1', 'item2']

# Access specific item using index
print("First item in key3 list:", my_dict['key3'][0])  # Output: item0

# Apply string method to item
print("Uppercase version of first item:", my_dict['key3'][0].upper())  # Output: ITEM0


#Updating Values in a Dictionary

# Check value before subtraction
print("Original value in key1:", my_dict['key1'])  # Output: 123

# Subtract 123 from key1
my_dict['key1'] = my_dict['key1'] - 123
print("Value after subtraction:", my_dict['key1'])  # Output: 0

# Use -= shortcut
my_dict['key1'] -= 123
print("Value after using -=:", my_dict['key1'])  # Output: -123

d = {'k1': 100,'k2':200}
print("Access keys:", d)
d['k3']=300
print("Access keys:", d)

#🌱 Creating Keys via Assignment
# Start with an empty dictionary
d2 = {}

# Assign key-value pairs
d2['animal'] = 'Dog'
d2['answer'] = 42

# Print entire dictionary
print("Dictionary after assignment:", d2)  # Output: {'animal': 'Dog', 'answer': 42}

#🪆 Nesting Dictionaries

# Nested dictionary example
d = {
    'key1': {
        'nestkey': {
            'subnestkey': 'value'
        }
    }
}

#exp2-🧪 1. Simple Nested Dictionary
student = {
    "name": "Sai krishna",
    "grades":{
        "math": 90,
        "science":85
    }
}
print(student['grades']['science'])
print(student['name'])

#exp3-🏡 2. Dictionary with Address Detail
person = {
    "name": "krishna",
    "address":{
        "street":"123 main st",
        "city":"Chicago",
        "zip":60005
    }
}
print('name is',person["name"],'and the address is ',person['address']['street'])

#📦 3. Inventory Tracker
inventory = {
    "item1": {
        "name": "Laptop",
        "quantity": 10,
        "price": 60000
    },
    "item2": {
        "name": "Mouse",
        "quantity": 50,
        "price": 500
    }
}
print(inventory["item2"]["price"])  # Output: 500

#🌐 4. API Response Style
api_response = {
    "user": {
        "id": 101,
        "details": {
            "username": "tech_guru",
            "email": "guru@example.com"
        }
    }
}
print(api_response["user"]["details"]["username"])  # Output: tech_guru

# Access nested value
print("Nested value:", d['key1']['nestkey']['subnestkey'])  # Output: value

#🧰 Basic Dictionary Method

# Typical dictionary
d = {'key1': 1, 'key2': 2, 'key3': 3}

# Get all keys
print("Keys:", list(d.keys()))  # Output: ['key1', 'key2', 'key3']

# Get all values
print("Values:", list(d.values()))  # Output: [1, 2, 3]

# Get all items as (key, value) tuples
print("Items:", list(d.items()))  # Output: [('key1', 1), ('key2', 2), ('key3', 3)]

