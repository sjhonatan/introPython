"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:35:35 2017
Number of code lines: 
13
"""
import random 

def rollDice():
    return random.choice([1,2,3,4,5,6])

def testRoll(trials = range(10)):
    result = ''
    for i in trials:
        result += str(rollDice())
        yield result

x = testRoll()
print(list(x))
