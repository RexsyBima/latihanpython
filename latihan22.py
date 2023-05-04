#Coding Exercise 1
names = ["john smith", "jay santi", "eva kuki"]

#Extend the code above so the code capitalizes all the names 
##and the surnames of the list and then prints the new list.

#the output of your code should be as below:
#['John Smith', 'Jay Santi', 'Eva Kuki']

names = [name.title() for name in names]
print(names)

#Coding Exercise 2
usernames = ["john 1990", "alberta1970", "magnola2000"]
#Extend the code above so the code 
#prints out a list containing the number of characters for each username.
usernames = [len(user) for user in usernames]
print(usernames)

#Coding Exercise 3
user_entries = ['10', '19.1', '20']
#Extend the code above so the code 
#prints out a list containing the same items as floats.
user_entries = [float(user) for user in user_entries]
print(user_entries)

#Coding Exercise 4
user_entries_2 = ['10', '19.1', '20']
#Extend the code above so the code prints out the sum of the numbers.
# The output of your code should be as below:
#49.1
user_entries_2 = [float(user) for user in user_entries_2]
print(sum(user_entries_2))

#Bug-Fixing Exercise 1
# The code below tries to write the items of temperatures each in one line 
# in the file.txt list. However, the code has an error. Try to fix the error.

temperatures = [10, 12, 14]
file = open("temp.txt", 'w')
for temperature in temperatures:
    file.writelines(str(temperature)+ '\n')
file.close()

#Bug-Fixing Exercise 2
#he code below tries to convert all the numbers to integers. 
# However, the code has an error. Try to fix the error.

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)