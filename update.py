"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 21:07:18 2017
Number of code lines: 
125
"""
import sys 
import os
import time
import subprocess
import glob
import subprocess

def main():
    u = Update()
    arg = sys.argv 
    if len(arg) > 1:
        if arg[1] == 'all':
            u.getAllFilesUpdated()
        else:
            u.getUpdate()


class Update():

    def __init__(self):
        self.time = str(time.asctime(time.localtime(time.time())))
        self.numberOfLines = 0
        self.lines = []
        self.name = ''
        self.arg = ''
        self.ext = ''
        self.ext1 = ''
        self.updateFile = []
        self.vim = False

        """ for all files purposes """
        self.pythonFiles = []
        self.directories = []
        self.currentPath = ''

    def getArgument(self):
        vim = False
        if len(sys.argv) < 2:
            raise ValueError('You must give an argument,\
                             e.g, filename')
        else:
            self.arg = sys.argv[1]
        
        if '.py' in self.arg:
            self.ext = '"""'
            self.ext1 = '"""'
        elif 'vimrc' in sys.argv[1]:
            self.ext = '"'
            self.ext1 = '"'
            self.updateFile = ['"Vimrc File', 
                               '"Jhonatan da Silva',
                               '"Last Updated version :',
                               '"'+str(self.time),
                               '"Number of code lines :',
                               ]
            self.vim = True
        else:
            self.ext = '/*'
            self.ext1 = '*/'

        if not self.vim:
            self.updateFile = [self.ext,
                                'Jhonatan da Silva',
                                'Last Updated version :', 
                                str(self.time) ,
                                'Number of code lines: ',
                                self.ext1] 

    def createFile(self, data):
        with open('temp.py','w') as temp:
 
            if self.vim:
                for words in self.updateFile:
                    temp.write(words)
                    temp.write('\n')
                temp.write('"'+str(self.numberOfLines))
                temp.write('\n')
                temp.write(self.ext1)
                temp.write('\n')
                for words in data:
                    temp.write(words)
                    temp.write('\n')

            if not self.vim:
                last = False
                for words in self.updateFile:
                    if self.ext1 in words:
                        if last:
                            temp.write(str(self.numberOfLines))
                            temp.write('\n')
                            temp.write(self.ext1)
                            temp.write('\n')
                        else:
                            temp.write(self.ext1)
                            temp.write('\n')
                    else:
                        temp.write(words)
                        temp.write('\n')
                        last = True
                for words in data:
                    temp.write(words)
                    temp.write('\n')

        f = 'rm -rf ' + self.name
        subprocess.call(f,shell=True) 
        f = 'mv ' + 'temp.py ' + self.arg
        subprocess.call(f,shell=True)
    
    def getUpdate(self,name=None):
        self.getArgument()
        name = self.arg
        #self.name = name 
        with open(os.path.abspath(name),'r') as f:
            data = f.read().splitlines()
            found = False
            n = self.updateFile[1]
            for words in data[:10]:
                if n == words:
                    found = True
                    index = data.index(n)
                    break
            if found:
                while(data[index] != self.ext1):
                    index += 1
                for words in data[index+1::]:
                    self.lines.append(words)
                    self.numberOfLines +=1

                self.createFile(self.lines)

            else: 
                self.numberOfLines = len(data)
                self.createFile(data)
            
    def getAllFilesUpdated(self):
        for names in os.listdir():
            if '.' not in names[0]:
                self.directories.append(names)

        """for eachName in self.directories:
            try:
                self.current = os.getcwd()
                os.chdir('./' + eachName)
                python = glob.glob("*.py")
                if len(python) > 0:
                    for eachFile in python:
                        f = '~/anaconda3/bin/python ' +\
                            './../update.py ' + eachFile
                        print(f)
                        subprocess.call(f,shell=True)
                        f = 'sudo git add ' + eachFile
                        print(f)
                        subprocess.call(f,shell=True)
                        f = 'sudo git cm -m "update"'
                        print(f)
                        subprocess.call(f,shell=True)
                        #subprocess.call(f,shell=True)
                os.chdir(self.current)
            except Exception as e:
                pass""" 
        for eachName in glob.glob("*.py"):
            self.current = os.getcwd()
            python = glob.glob("*.py")
            f = '~/anaconda3/bin/python ' +\
                './../update.py ' + eachName
            print(f)
            subprocess.call(f,shell=True)
            f = 'sudo git add ' + eachName
            print(f)
            subprocess.call(f,shell=True)
            f = 'sudo git cm -m "update"'
            print(f)
            subprocess.call(f,shell=True)
 
if __name__ == '__main__':
    main()
