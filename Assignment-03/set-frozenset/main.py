# set data type 
# set is a collection of items that are unique and unordered
# set is defined by curly braces {}
# set is unindexed (no index)
# set is unordered (no order)
# set is unhashable (no hash value)
# A set can store only immutable objects such as number 
# (int, float, complex or bool), string or tuple. If you try to put
#  a list or a dictionary in the set collection, Python raises a TypeError.

my_set = { 1, 2, 3, 4, 5 }
print(my_set)

my_set2 = {1 ,2 ,3 ,4 ,5 ,6,1 ,3 , 5 }
print(my_set2) # ignore duplicate

sets = {"mahnoor" , 20 , 1.2 , True}
print(sets) # hold different data type

# setss_error = {1 , 2 , 3 , "Mahnoor" , True , ["john" , "doe"]}
# print(setss_error) # error because list is mutable

set2: set = {'Java', 'Python', 'JavaScript', 'java'}
print(set2)  # and unordered 

try:
    set2[2] = "C++"
except TypeError:
    print("We can't add list to set because list is mutable")

# add item to set
set2.add("C++")
print(set2) # add item to set

set2.remove("Java")
print(set2) # error if item not found

set2.discard("python")
print(set2) # no error if item not found

set2.pop()
print(set2) # remove last item

# frozenset examples
# frozenset is an immutable version of set
# once created, elements cannot be modified
# useful as dictionary keys or in other sets

# Creating frozensets
fruits = frozenset(['apple', 'banana', 'orange'])
numbers = frozenset([1, 2, 3, 4, 5])
mixed = frozenset(['Python', 42, 3.14, True])

print("\nFrozenset Examples:")
print("Fruits frozenset:", fruits)
print("Numbers frozenset:", numbers)
print("Mixed frozenset:", mixed)

# frozenset operations (non-modifying)
print("\nFrozenset Operations:")
print("Length of fruits:", len(fruits))
print("Is 'apple' in fruits?", 'apple' in fruits)
print("Union of fruits and numbers:", fruits.union(numbers))
print("Intersection of fruits and numbers:", fruits.intersection(numbers))

# Using frozenset as dictionary key
dictionary = {
    fruits: "Fruit Collection",
    numbers: "Number Collection"
}
print("\nDictionary with frozenset keys:", dictionary)

# Note: These operations will raise AttributeError
# fruits.add('grape')  # Can't add
# fruits.remove('apple')  # Can't remove
# fruits.pop()  # Can't pop     





