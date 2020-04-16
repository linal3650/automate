import random

guess = ""

def coinToss(guess):
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    toss = random.randint(0, 1) #0 is tails, 1 is heads
    if guess == 'heads':
        guess = int(1)
    elif guess == 'tails':
        guess = int(0)

    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()

        if guess == 'heads':
            guess = int(1)
        elif guess == 'tails':
            guess = int(0)

        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

coinToss(guess)
