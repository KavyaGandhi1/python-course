# astrologer star

# if boolean variable's value is true then print n like this
# *
# **
# till n

# and variable's value is false then print n - number like this
# **
# *
# till 1

# Solution

n = int(input('Enter how many row you want to print: '))
boolean = int(input('type 1 or 0: '))

if boolean==1:
     for i in range(n+1):
         print('*'*i)
elif boolean==0:
    for i in range(n+1):
        print('*'*(n-i))
else:
    print('You have to enter 1 or 0.')