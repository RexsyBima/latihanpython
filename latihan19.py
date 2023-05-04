files = ['a.txt', 'b.txt', 'c.txt']

for file in files:
    file = open(file, 'r')
    file = file.read()
    print(file)