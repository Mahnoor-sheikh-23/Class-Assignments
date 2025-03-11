# if else elif statement
money_spend = int(input("Enter the amount of money you spend in shopping : "))
if money_spend > 500:
    print("You got a 30% discount")
elif money_spend >= 200 and money_spend <= 500:
    print("You got a 20% discount")
elif money_spend < 200:
    print("You got a 10% discount")
else:
    print("No discount")


# while  loop 
num = 0
while num < 10 :
    num +=1 
    print( f"5 * {num} = {5 * num}")

# for loop 
fruits = ["apple", "banana", "cherry" , "orange" , "kiwi" , "mango" , "pineapple" , "strawberry"]
for x in fruits:
    print(x)

# Nested for loop
for x in range(1 , 10+1):
    for y in range(1,10+1):
        print(f"{x} * {y} = {x * y}")
    print("--------------------------------")
    
# nested if else 
cards = ["Visa Card" , "Master Card" , "American Express" , "Discover Card" , "Rupay Card" , "unionPay Card"]
print("Cards available in the market : ")
for i in cards:
    print(i)
user_card =  input("Enter the number or name of your card : ")
if user_card in cards:
    pin = int(input("Enter your pin :"))
    if pin == 98765:
        print(" ---------- Wellcome To Your Account ----------")
        balance = int(input("Enter the amount for withdraw :"))
        if balance <= 1000:
            print("Suffieicnt Balance is Availabe 😇 ")
            print(f"Your Remaining Balance is {1000 - balance} ❕ ")
            print(" ---------- Thank You For Using Our Service 😇 ----------")
        else:
            print("Insufficient Balance ❌")
    else:
        print("Invalid Pin ❌")
else:
    print("Invalid Card Type ❌")


