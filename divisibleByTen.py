# Divisible by ten randomizer
# Author: Marcel Willis
from random import randrange

def divisibleByTen():
    print("I generate numbers from 1 to 100 until I pick one divisible by 10.")
    remainder = 1
    
    while remainder != 0:
        randnum = randrange(0,100) + 1
        print(randnum)
        remainder = randnum % 10
    print("I'm done!")
    
divisibleByTen()
    
