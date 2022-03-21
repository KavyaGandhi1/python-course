# Guess the number

# no. of guess 9
#  print no.of guess left
# No. of guess he took to finish

guess_left = 6
n = 72
while(guess_left>0):
    num = int(input('Guess the number between 1 and 100: '))
    if num>n and guess_left>0:
        print('You have enter greater number.')
        guess_left = guess_left - 1
        print('No of guesses left is',guess_left)
        continue
    elif num<n and guess_left>0:
        print('You have enter smaller number.')
        guess_left = guess_left - 1
        print('No of guesses left is',guess_left)
        continue
    elif num==n and guess_left>0:
        print('Congrats , You have guessed correct number.')
        print('You took',(9-guess_left)+1,'chance to guess the number')
        break


if(guess_left==0):
    print('You lose the game')
