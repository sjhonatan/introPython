""" Inheritance """

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

class IFSCPerson():
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self,name)
        self.idNum = IFSCPerson.nextIdNum
        IFSCPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

person1 = IFSCPerson('Python Test')
print(person1.getIdNum())
