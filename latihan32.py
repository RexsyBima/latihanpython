#Coding Exercise 1
# Build a percentage calculator that 
# gets from the user the "total value" and the "value" and returns the percentage as shown below:
try:
    user_total_value = int(input("Enter total value : "))
    value            = int(input("Enter value : "))
    in_percent = value / user_total_value * 100
    print(f"{in_percent} %")
except ValueError:
    print("Yoy need enter a number. run the program again")
except ZeroDivisionError:
    print("Your total value cant be zero")
    
#Coding Exercise 2
# As you might know, it is not mathematically possible to divide a number by zero. 
# Consequently, this is also not possible in Python either -
# you will get a ZeroDivisionError if you try:
#With that in mind, your task for this exercise is to extend the program you 
# created in Exercise 1 by displaying a message to the user 
# when they enter 0 for the "total value".

#Bug-Fixing Exercise 1
#Have a look at the program below:#
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")
    
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    exit(f"{name} is not in the list")
#When the user enters the name of one of the waiting_list members, 
# the program returns the index of that name. 
# For example, when the user enters "john", 0 is printed out.
#If the user enters a name that is not in the list, such as "zen", 
# the program throws an error.

#Change the program, so it prints out "zen is not in the list" 
# instead of returning an error when the user enters "zen" 
# or any other name that is not in the list.