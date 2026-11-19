import random

def getRandomNumber(lowest, highest):
    return random.randrange(lowest, highest)

randnum = getRandomNumber(1, 100)
print(getRandomNumber(1, 100))

guess = input('Guess: ')