try:
    width = float(input("Rectangle width : "))
    length = float(input("Rectangle length : "))
    if type(width) == float and type(length) == float:
        exit("we dont accept square calculation")

except ValueError:
    print("please enter width and length in number")
    exit()
except NameError:
    print("please enter width and length in number")
    exit()


area = width * length
print(area)