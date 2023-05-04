new_member = input("Add a new member : ")

file = open('members.txt', 'r')
file_list = file.readlines()
file.close()

file_list.append(new_member + '\n')

file = open('members.txt', 'w')
file.writelines(file_list)
file.close()