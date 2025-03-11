# list  and its methods
# list is a collection of items (can contain different types of data)
# list is ordered and mutable (can be changed)
# list is indexed (can be accessed by index)
# list is iterable (can be looped through)
# list is heterogeneous (can contain different types of data)
# list is mutable (can add or remove items)
# list is dynamic (can add or remove items)

names = ["John", "Jane", "Jim", "Jill" , "Jack"]
print(names) # print all names
print(names[3]) # print the 4th name
print(names[-1]) # print the last name
names[3] = "herry" # change the 4th name
print(names)
print(names[1:5])
 # print the 2nd to 5th name
names.append("Abacus") # add a new name
print(names)

names.remove("John") # remove a name
print(names)

names.pop(2) # remove the 3rd name
print(names)

names.pop() # remove the last name
print(names)

names.clear() # remove all names
print(names)

names.insert(0, "John") # insert a name at the beginning
print(names)

names.insert(2, "Jane") # insert a name at the 3rd position
print(names)

names.sort() # sort the names
print(names)

names.reverse() # reverse the names
print(names)

names.count("John") # count the number of John
print(names)

names.index("John") # find the index of John
print(names)


# Tuple 
# these are immutable (cannot be changed)
# these are ordered and indexed (can be accessed by index)
# these are iterable (can be looped through)
# these are heterogeneous (can contain different types of data)
# these are dynamic (can add or remove items)   

tuple1 = ("apple", "banana", "cherry","pineapple","strawberry")
tuple2 = ("onion", "garlic", "potato","carrot","beans" , "peas")
tuple3 = tuple(["rose", "rose" ,  "lily", "tulip","daisy","sunflower"])
tuple4 = tuple1 + tuple2
print(tuple3)
print(tuple2[2])
print("id of tuple1 is : ", id(tuple1))
print("id of tuple2 is : ", id(tuple2))
print("id of tuple3 is : ", id(tuple3))
print(tuple1 == tuple2)
print(tuple3[0])
print(tuple3[0:4])
print(len(tuple3))
print(tuple3.count("rose"))
print(tuple3.index("rose"))



# DICTIONARY 
# these are mutable (can be changed)
# these are unordered and unindexed (cannot be accessed by index)
# these are iterable (can be looped through)
# these are heterogeneous (can contain different types of data)
# these are dynamic (can add or remove items)

info = {
    "name": "John",
    "age": 20,
    "city": "New York"
}
print(info)
print(info["name"])
print(info["age"])
print(info["city"])

info["age"] = 21
print(info)

info["city"] = "Los Angeles"
print(info)

del info["city"]
print(info)

print(info.keys())
print(info.values())
print(info.items())

info.update({"city" :"California"})
print(info)

for value in info.values():
    print(value)

for key , value  in info.items():
    print( key ,":" , value)


# Nest
person  = {
    "name": "John",
    "age": 20,
    "city": "New York",
    "skills": ["Python", "Java", "C++"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}

print(person)
print(person["address"]["city"])

person2 = person.copy()
print(person2)

person2["name"] = "Jane"
print(person2)

person2["skills"].append("SQL")
print(person2)





































