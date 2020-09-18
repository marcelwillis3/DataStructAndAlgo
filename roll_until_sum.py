# Dice Roll Until Sum Simulator
# Author: Marcel Willis
from random import randrange

def rollDice():
    # Method to roll a six-sided dice and return the value
    dieValue = randrange(1,7)
    return dieValue

def getSum(firstValue,secondValue):
    # Method to add two values and return the result
    total = firstValue + secondValue
    return total

def main():
    print("This program rolls two 6-sided dice until their sum is a given target value.")
    targetSum = int(input("Enter the target sum to roll for: "))
    print('')
    
    rollSum = 0
    rollCount = 0
    while rollSum != targetSum:
        rollCount += 1
        die1Value = rollDice()
        die2Value = rollDice()
        rollSum = getSum(die1Value,die2Value)
        print("Roll: {0} and {1}, sum is {2}".format(die1Value,die2Value,rollSum))
    print("Got it in {} rolls!".format(rollCount))
    
main()