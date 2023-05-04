password_input = input("please enter your password : ")
result = {}
if len(password_input) >= 8:
    result['length'] = True
elif len(password_input) < 8:
    result['length'] = False

upper = False
for i in password_input:
    if i.isupper():
        upper = True
        result['Upper'] = upper
    elif upper == False:
        result['Upper'] = False

digit = False
for digit in password_input:
    if digit.isdigit():
        digit = True
        result['digit'] = digit
    elif digit == False:
        result['digit'] = False
print(result)

if result['length'] == True and result['Upper'] == True and result['digit'] == True:
    print("this is strong password")
else:
    print("This is weak password")

if all(result.values()):
    print("str pass")