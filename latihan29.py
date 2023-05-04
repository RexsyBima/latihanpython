password_input = input("please enter your password : ")
result = []
if len(password_input) >= 8:
    result.append(True)
if password_input.isupper():
    result.append(True)
if password_input.isdigit():
    result.append(True)
else:
    print("This is weak password")
    exit()
for i in result:
    if i == True:
        print("this is strong password")