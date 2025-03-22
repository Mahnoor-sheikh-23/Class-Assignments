# Modules
# There are three types of modules in Python:
# 1. Built-in modules
# 2. User-defined modules
# 3. Third-party modules


# Built-in modules
print("The print function is Built-in module in python ")

# user defined modules
from app import main
main()

# Third-party modules
# like request ,numpy , pandas etc


# FUNCTIONS IN PYTHON
def my_func():
    print("Hello from my_func")
my_func()


# FUNCTION ARGUMENTS
def arg_func(name):
    print(f"Hello {name}")
arg_func("john")
arg_func("william")

# Keyword arguments
# means that the function call identifies the arguments by the parameter name.
def key_func(name , age):
    print(f"Hello {name} your age is {age}")
key_func(age=29 , name="john")

# default arguments
def default_func(name="bob"):
    print(f"Hello {name}")
default_func()
default_func("william")


# unpacking arguments
# Returning multiple values by default results in a tuple

def unpack_func(*nums):
    print(nums)
list1 = [2,3,4,5,6,7]
unpack_func(*list1)


# Positional-only arguments
# positional-only arguments are defined using a slash (/) in the function definition.
def pos_func(name,fname,/,city):
    print(f"Hello {name} {fname} from {city}")

pos_func("john","william",city="new york")# run perfectly 
pos_func("john","william","Belgium") 
# pos_func("john","william",name="new york")                # this will cause error 
# pos_func(name="john",fname="william",city="new york")     # this will also cause error


# KEY WORD ONLY ARGUMENTS 
def kew_func(*,name , fname , lname , age , city):
    for i in name , fname , lname , age , city:
       
        print(i)

kew_func(name="john",fname="william",lname="smith",age=29,city="new york")


# VARIABLE LENGTH ARGUMENTS
def var_func(arg1 , *arg2):
    print("This is gping to be first argument ",arg1)
    print("This is going to be rest ",arg2)

var_func(20 , 100 , 300 , 400 , 500)




# RETURNING VALUES
#  it is used to return values from a function. so that we can use that value in other parts of the code. 
#  it only return a value not print it.
def return_func():
    return "Hello from return_func"

variable = return_func()
print(variable)



# LAMBDA FUNCTIONS OR ANONYMOUS FUNCTIONS
# Lambda functions are small, anonymous functions that are defined using the lambda keyword.

small_func = lambda name :   name * 3 
print(small_func("john" + " "))

my_dic = {"apple":100 , "banana":200 , "cherry":300 , "date":400}

dic_func = sorted(my_dic.items(), key=lambda x:x[1])
print(dic_func)



# KWARGS
# The **kwargs parameter in a function is used to pass a keyworded, variable-length argument list.  
def kwargs_func(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

kwargs_func(name="john",fname="william",lname="smith",age=29,city="new york")


# RECURSION
# Recursion is a technique in which a function calls itself to solve a problem.
# The base case is the condition that stops the recursion.
# The recursive case is the condition that continues the recursion.
# Recursion is a powerful tool, but it can be computationally expensive.
# Recursion can be used to solve problems that can be broken down into smaller, similar problems.
def rec_func(n):
    if n == 1:
        return 1
    else:
        return n * rec_func(n-1)
print(rec_func(4))



# Generators
# Generators are functions that return an iterable sequence of items.
# Generators are used to create iterators.
# Generators use the yield keyword to return items one at a time.
# Generators are more memory efficient than lists.
def gen_func(n):
    for i in range(n):
        yield i
for i in gen_func(6):
    print(i)


