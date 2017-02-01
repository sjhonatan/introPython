"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:47:21 2017
Number of code lines: 
21
"""
import os 
import glob
directories = []
pythonFiles = []
for names in os.listdir():
    if '.' not in names[0]:
        directories.append(names)

for eachName in directories:
    try:
        current = os.getcwd()
        os.chdir('./' + eachName)
        python = glob.glob("*.py")
        if len(python) > 0:
            pythonFiles.extend(python)
     
    except Exception as e:
        pass
    os.chdir(current)

print(pythonFiles)
