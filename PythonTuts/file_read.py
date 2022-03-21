f = open('kavya.txt')

# content = f.read(10)  # used to read a file
# print(content)
# content = f.read()
# print(content)


# for line in f:
#     print(line)

# print(f.readline())    # this func is used to read a line in file
# print(f.readline())

print(f.readlines())  # this func is used to make list of lines
f.close()

