#design a faulty calculator which will calculate all the answers correctly execpt
# 45*3 = 555 , 56+9 = 77 , 56/6 = 4

num1 = int(input('Enter first number: '))
num2 = int(input('Enter Second number: '))
operator = input('Enter the operator to perform calculation(+,-,*,/): ')
if num1==45  and  num2==3 and operator=="*":
    print('555')
elif num1==56 and num2==9 and operator == "+":
    print(77)
elif num1==56 and num2==6 and operator=="/":
    print(4)
elif operator == '+':
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == '*':
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
else:
    print('out of range')