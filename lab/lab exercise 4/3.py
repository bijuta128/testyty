
import random
num, guessnum = random.randint(1, 10), 0
while num != guessnum:
    guessnum = int(input('Guess a number between 1 and 10 : '))
print('done')