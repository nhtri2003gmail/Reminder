import datetime
import time
import sys
import os


newUserPath=''
with open('C:\\Program Files\\Reminder\\userPath.txt', 'rt') as f:
    userPath = f.read()
for i in range(1, len(userPath)-2):
    newUserPath+=userPath[i]
dateLocation = 'C:\\' + newUserPath + '\\Documents\\Reminder'
print(dateLocation)
os.chdir(dateLocation)

dateSave = os.listdir(dateLocation)
if dateSave==[]:
    sys.exit()
    

def DayMonthYear():
    now = str(datetime.datetime.now())
    today = now.split(' ')
    
    t = str(today[0])
    date = t.split('-')
    
    return date[2] + '-' + date[1] + '-' + date[0]

def Operate():
    print(dateSave)
    for i in dateSave:
        NameType = str(i).split('.')
        fileName = str(NameType[0])
        if fileName==DayMonthYear():
            fullName = str(i)
            os.startfile(fullName)

def Del():
    now = DayMonthYear()
    today = now.split('-')
    preDay = int(today[0])-1
    preDate = str(preDay) + '-' + today[1] + '-' + today[2]
    
    for i in dateSave:
        NameType = str(i).split('.')
        fileName = str(NameType[0])
        if fileName == preDate:
            fullName = str(i)
            os.system(f'del {fullName}')    

if __name__ == '__main__':
   Del()
   Operate()
   
