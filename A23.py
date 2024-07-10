try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("File not found.")
else:
    print(file.read())
    file.close()
