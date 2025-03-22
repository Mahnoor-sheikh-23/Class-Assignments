import time
import calendar
from datetime import datetime
import math 

# Get the current date and time
now = datetime.now()

# Print the current date and time in different formats
print("Current Date and Time:", now)  
print("Formatted Date:", now.strftime("%Y-%m-%d %H:%m:%S"))  # Output: 2025-03-22 14:30:45

# CALENDER 

# Get the number of days in a specific month and year
year = 2025
month = 2  # February
days_in_month = calendar.monthrange(year, month)[1]
print(f"Days in {calendar.month_name[month]} {year}: {days_in_month}")  # Output: 28

# Get the calendar for a specific month and year
cal = calendar.month(2025, 3)
print(cal)

localtime = time.localtime(time.time())
more = time.asctime(localtime)
print ("Local current time :", more)
print ("Local current time :", localtime)

# MATH MODULE
#  we have the math module in Python which provides various mathematical functions.
#  Some of the commonly used functions are:
print("Squre root of 16 ",math.sqrt(16))  
print("Cube  of 2 ",math.pow(2, 3))  
print("Pie value ",math.pi)  
print(math.e) 
print(math.sin(math.radians(30)))  
print(math.cos(math.radians(60)))  
print(math.tan(math.radians(45)))  
print(math.factorial(5))  
print(math.ceil(2.4))
print(math.floor(2.4))
print(math.log(10))  
print(math.tau)   # 2 * pi
print(math.inf)   # infinity
print(math.nan)   # not a number
print(math.isfinite(10))
print(math.isfinite(99999999999999999999999999999999999999999999))