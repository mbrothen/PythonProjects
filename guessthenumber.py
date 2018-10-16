#guess the number
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#give 6 guesses
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #right guess
if guess == secretNumber:
    print('Good job! you guessed the number in ' +str(guessesTaken) + ' guesses!')
else:
    print('Nope.  The number I was thinkin of was ' + str(secretNumber))
