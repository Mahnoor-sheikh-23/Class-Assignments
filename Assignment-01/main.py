# DATA_TYPES........
# 01_STRING("",'',"""""")
name="String"
print(type(name))

assign = '1'
print(assign)

day_1 = """Amazing
Class"""
print(day_1)

# 02_INTIGER 1 , 2 
num = 1
print(type(num))

# 03_BOOLEAN True/False
is_Working = True
print(type(is_Working))

# 04_FLOAT 3.5,45.99...
assign_Done = 50.9
print(type(assign_Done))

# 05_LIST [1,2,3,4,...] or ["is","an ","the",...]
assign_01 = ["Data Types","Python Keywords","Make X Account","Study Google Collab on Youtube"]
print(type(assign_01))

# 06_TUPLE (Its also like an array but its immutable cant change it)
fruits = ("Apple", "Mango", "Grapes")
print(type(fruits))

# 07_SETS (sets items are unordered, unchangeable and do not allow duplicate values)
this_Fruits = {"Apple", "Mango", "Grapes", "Apple"}

# Duplicated values will be ignored
print(type(this_Fruits))

# 08_DICTIONARIES (Its store data values in key:values pair form like)
data = {
    "day" : "Monday",
    "time" : "2 to 5",
    "teacher" : "Asharib Ali"
}
print(type(data))

# 09_FROZENSET (same as set but immutable)
flowers = {"Rose", "Sunflower", "Lily", "Daisy"}
print(type(flowers))

# 10_NONETYPE 
x = None
print(type(x))