def get_greeting(country):
    if country == "USA":
        return "Hello"
    elif country == "INDIA":
        return "Namaste"
    elif country == "JAPAN":
        return "Konnichiwa"
    else :
        return "Greetings"

def convert_to_euros(amount, country):
    if country == "USA":
        return amount * 0.85
    elif country == "INDIA":
        return amount * 0.012
    elif country == "JAPAN":
        return amount * 0.006

print("welcome to currency to euro converter. we only support USA, India, and Japan")
name_depan = input("what is your first name : ")
name_belakang = input("what is your last name : ")
country = input("where are you from : ").upper()

print(f"{get_greeting(country)}, {name_depan.capitalize()} {name_belakang.capitalize()}")
if get_greeting(country) == "Greetings":
    print("Sorry, we only support USA, India, and Japan at the moment.")
    exit()

amount = float(input("Enter the amount of your local currency here : "))
def currency_print(country):
    if country == "USA":
        return "$"
    elif country == "INDIA":
        return "Rupee"
    elif country == "JAPAN":
        return "Yen"

print(f"the amount of {int(amount)} {currency_print(country)} to Euro is {int(convert_to_euros(amount, country))} Euro")