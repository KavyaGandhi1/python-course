# Health Management System
# 3 clients - Harry, Rohan and Hammad
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# Solution
def getdate():
    import datetime
    return datetime.datetime.now()

def log(a,b):
    data = input('Enter the data: ')
    if a=='Harry' and b==1:
        f = open('HarryDiet.txt','a')
        f.write(str(getdate())+' '+data + '\n')
        print('Succesfully Entered')
        f.close()
    elif a=='Harry' and b==2:
        f = open('HarryExercise.txt','a')
        f.write(str(getdate())+' '+data + '\n')
        print('Succesfully Entered')
        f.close()
    elif a=='Rohan' and b==1:
        f = open('RohanDiet.txt','a')
        f.write(str(getdate())+' '+data + '\n')
        print('Succesfully Entered')
        f.close()
    elif a=='Rohan' and b==2:
        f = open('RohanExercise.txt','a')
        f.write(str(getdate())+' '+data + '\n')
        print('Succesfully Entered')
        f.close()
    elif a=='Hammad' and b==1:
        f = open('HammadDiet.txt','a')
        f.write(str(getdate())+' '+data + '\n')
        print('Succesfully Entered')
        f.close()
    elif a=='Hammad' and b==2:
        f = open('HammadExercise.txt','a')
        f.write(str(getdate())+'  '+data + '\n')
        print('Succesfully Entered')
        f.close()
    else:
        print('Invalid Input')

def retrive(a,b):
    if a=='Harry' and b==1:
        f = open('HarryDiet.txt')
        print(f.read())
        f.close()
    elif a=='Harry' and b==2:
        f = open('HarryExercise.txt')
        print(f.read())
        f.close()
    elif a=='Rohan' and b==1:
        f = open('RohanDiet.txt')
        print(f.read())
        f.close()
    elif a=='Rohan' and b==2:
        f = open('RohanExercise.txt')
        print(f.read())
        f.close()
    elif a=='Hammad' and b==1:
        f = open('HammadDiet.txt')
        print(f.read())
        f.close()
    elif a=='Hammad' and b==2:
        f = open('HammadExercise.txt')
        print(f.read())
        f.close()
    else:
        print('Invalid Input')

print('Welcome to Health Management System')
name = input('Enter Client\'s Name: ')
type = int(input('Enter 1 for diet and 2 for exercise: '))
num = int(input('Enter 1 to log or 2 to retrive data: '))

if num==1:
    log(name.lower().capitalize(), type)
elif num==2:
    retrive(name.lower().capitalize(),type)
else:
    print('Invalid input')




