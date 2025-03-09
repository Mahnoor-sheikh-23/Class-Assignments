# 01  (ARITHEMATIC OPERATORS )

# + , - , * , / , % , ** , //

# Examples with meaningful variables
price = 100
tax_rate = 0.2
quantity = 5

total_price = price * quantity  # Multiplication: 500
tax_amount = total_price * tax_rate  # Multiplication with decimal: 100
final_price = total_price + tax_amount  # Addition: 600
discount = 50
discounted_price = final_price - discount  # Subtraction: 550

# Power and Division examples
square_meters = 4
area_squared = square_meters ** 2  # Power: 16
items_per_box = 7
boxes_needed = 20 // items_per_box  # Floor division: 2
remaining_items = 20 % items_per_box  # Modulus: 6


# 02 (ASSIGNMENT OPERATORS )

# = , += , -= , *= , /= , %= , **= , //=

# Examples with a running total
score = 0  # Initial assignment
score += 10  # score is now 10
score -= 3   # score is now 7
score *= 2   # score is now 14
score /= 2   # score is now 7.0
bonus = score
bonus **= 2  # bonus is now 49.0
bonus //= 5  # bonus is now 9.0


#  03 (COMPARISON OPERATORS )

# == , != , > , < , >= , <=

# Examples with age verification
age = 18
is_adult = age >= 18  # True
can_drink = age > 21  # False
is_teen = age < 20  # True
is_child = age <= 12  # False
is_exactly_18 = age == 18  # True
is_not_21 = age != 21  # True

# 04 (LOGICAL OPERATORS )

# and , or , not

# Examples with user permissions
is_logged_in = True
is_admin = False
has_permission = True

can_edit = is_logged_in and has_permission  # True
can_delete = is_admin or has_permission  # True
is_guest = not is_logged_in  # False

# 05 (BITWISE OPERATORS )  

# & , | , ^ , ~ , << , >>

# Examples with binary operations
a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary

c = a & b   # AND: 12 (0000 1100)
d = a | b   # OR: 61 (0011 1101)
e = a ^ b   # XOR: 49 (0011 0001)
f = ~a      # NOT: -61
g = a << 2  # Left shift: 240 (1111 0000)
h = a >> 2  # Right shift: 15 (0000 1111)

# 06 (IDENTITY OPERATORS ) 

# is , is not

# Examples with object identity
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

same_list = list1 is list3      # True (same object)
different_list = list1 is list2  # False (different objects)
not_same = list1 is not list2   # True

#  07 (MEMBERSHIP OPERATORS )

# in , not in

# Examples with collections
fruits = ['apple', 'banana', 'orange']
has_apple = 'apple' in fruits           # True
no_mango = 'mango' not in fruits        # True
user_permissions = {'read', 'write'}
can_delete = 'delete' in user_permissions  # False






