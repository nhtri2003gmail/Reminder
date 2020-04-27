import os
import time
import sys

newUserPath=''
with open('userPath.txt', 'rt') as f:
    userPath = f.read()
for i in range(1, len(userPath)-2):
    newUserPath+=userPath[i]
dateLocation = 'C:\\' + newUserPath + '\\Documents\\Reminder'

while True:
    print("Do you want to delete your data?")
    print("1. Yes   2.No")
    c = input("Your answer: ")
    try:
        c = int(c)
    except:
        print('Wrong answer!!!')
        os.system('cls')
        continue
    if c==1 or c==2:
        break
    else:
        print('Wrong answer!!!')
        os.system('cls')

print('Deleting Reminder folder...')
os.chdir('C:\Program Files')
os.system('del /Q Reminder')

print('Deleting Reminder.lnk...')
os.system('cd C:\%HOMEPATH%\Desktop && del Set_Reminder.lnk')

print('Deleting Set_Reminder.exe...')
os.system('cd C:\%HOMEPATH%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup && del /Q Reminder.exe')

if c==1:
    print('Deleting data...')
    os.system(f'del /Q {dateLocation}')

print('Uninstall Completed')

print("Press Enter to exit...")
i=input()
