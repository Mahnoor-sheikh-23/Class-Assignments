# Exception hadling is a way to handle the runtime errors in a program.
# It is a way to handle the exceptions\error that are raised in a program.
# if we don't handle the exceptions, the program will terminate abruptly.
# There are two types of exceptions:
from typing import NoReturn
try:
    a = 10
    b = 20
    c = a/b
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Some error occured")
else:
    print("No error occured" , c)
finally:
    print("Finally block is always executed")

# try block use to write the code that may raise an exception.
# except block is used to handle the exception.
# else block is executed if no exception is raised.
# finally block is always executed whether exception is raised or not.


# RAISE AN EXCEPTION
# We can raise an exception using raise keyword.

try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    c = a/b
except ZeroDivisionError as e:
    print(e)
except:
    print("Some error occured")
else:
    print("No error occured" , c)
finally:
    print("Finally block is always executed")



#NORETURN
# The NoReturn type is used to indicate that a function does not return a value.
def func(a: int) -> NoReturn:
    print(a)  
func(10)
# func(10) will not return any value. It will just print the value of a. So, we can use NoReturn type to 
# indicate that the function does not return any value.


# here we can also use None type to indicate that the function does not return any value.
def func(a: int) -> None:
    print(a)
func(10)
# here also, func(10) will not return any value. It will just print the value of a. So, we can use None type to


