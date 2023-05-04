#Coding Exercise 1
#A client wants to buy a coin-flip probability program from you.

#The programs should work like this:

#1. The user runs the program. The program asks the user to enter "head" or "tail".
#The user flips a coin on their desk, table, floor, etc., 
# and then enters "head" or "tail". The user does the same over and over again.

#In each cycle, the program should return the current percentage of heads 
#in the program, similar to what you see in the screenshot
#above. Also, you should write each user entry (i.e., head or tail) in a text file
# using a with-context manager, one entry per line.

while True:
    with open('head_tail.txt', 'r') as file:
        file_read = file.readlines()
        print(file_read)
    head_tail = input("Throw the coin and enter head or tail here : ") +'\n'
    file_read.append(head_tail)
    
    with open('head_tail.txt', 'w') as file:
        file.writelines(file_read)
        
    heads = file_read.count("head\n")
    percentage = heads / len(file_read) * 100
    
    print(f"heads : {percentage}%")
        