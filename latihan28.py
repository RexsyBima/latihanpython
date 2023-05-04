#Coding Exercise 1
# Write a program that asks users to enter a password. 
# Then, it checks if the password length is greater than 7 
# and returns "Great password there!".
#If the password has 7 or fewer characters, the program returns, 
# "Your password is weak".

user_password = input("Enter a new password : ")
if len(user_password) > 7:
    print("Great password there")
elif len(user_password) == 7:
    print("Password is not too strong")
elif len(user_password) < 7:
    print("your password is weak")
    
   # Bug-Fixing Exercise 1: The program below intends to find out how many items 
   # have at least one underscore ("_") character in them.  
   # However, there is an error with the code. Try to find and fix it.

ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
for id in ids:
    if '_' in id:
        x = x + 1
print(x)

#Bug-Fixing Exercise 2: This program also intends to find out 
# how many items have an underscore in them. 
# However, the program has a bug. It doesn't return an error message, 
#the expected output is: 2

ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
for id in ids:
    if '_' in id:
        x = x + 1
print(x)

#Bug-Fixing Exercise 3: Fix the program below so it prints out "OK" 
# when the perimeter is less than 14 and the area is less than 8. 

length = float(input("Enter length: "))
width = float(input("Enter width: "))
 
perimeter = (length + width) * 2
area = length * width
 
print("Perimeter is", perimeter)
print("Area is", area)
 
if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")
