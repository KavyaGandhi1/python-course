a = 1
b = 2
c = sum((a,b))  # built in function
# print(c)


def func1(a,b):
    '''This function returns average of two numbers.'''
    avg = (a+b)/2
    return avg

average = func1(4,5)
print(average.__doc__)
print(average)
