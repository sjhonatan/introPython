import datetime

class Person():
    def __init__(self,name):
        self.name = name
        """ In case of no last name """
        try:
            """ Finds the last blank space in the string """
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except: 
            self.lastName = name
        '''
        """ If you want the full name after the first, you can use that """
        notFound = True 
        while notFound:
            for i in range(len(name)):
                if name[i] == ' ':
                    self.lastName = name[i+1:] 
                    notFound = False
        '''
        self.birthday = None

    def getLastName(self):
        return self.lastName

    def setBirthday(self):
        assert type(birthDate) == datetime.date
        self.birthday = birthDate

    def getAge(self):
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days
    
    """ When someone try to print this function will be called """  
    def __str__(self):
        return self.name

someone = Person('Python Test')
other = Person('C++ Language')
print(someone.getLastName())

peopleList = [someone, other]
print("\nNames : \n")
for name in peopleList:
    print(name)
