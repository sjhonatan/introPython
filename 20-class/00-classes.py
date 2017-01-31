# First we initiate the class
class Functions():
    def __init__(self):
        self.numFunctions = 3

    def firstFunction(self):
        print("I'm in the first function")

    def secondFunction(self):
        print("I'm in the second function")

    def numberFunctions(self):
        print(self.numFunctions)

F = Functions()

F.firstFunction()
F.secondFunction()
F.numberFunctions()
