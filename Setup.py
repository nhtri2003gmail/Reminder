import os
import time

remindPath = 'C:\Program Files\Reminder'

os.chdir('Setup')
if os.path.exists(remindPath):
    print("Folder Reminder exist")
else:
    print("Creating Reminder folder")
    os.mkdir(remindPath)
## Reminder.exe
print("Copying Reminder.exe...")
os.system('copy Reminder.exe \"C:\%HOMEPATH%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"')
## Set_Reminder.lnk
print("Copying Set_Reminder.lnk...")
os.system('copy Set_Reminder.lnk \"C:\%HOMEPATH%\Desktop\"')
## note.ico
print("Copying note.ico...")
os.system('copy note.ico \"C:\Program Files\Reminder\"')
## Set_Reminder.py
print("Copying Set_Reminder.py...")
os.system('copy Set_Reminder.py \"C:\Program Files\Reminder\"')
## StrOp.py
print("Copying StrOp.py...")
os.system('copy StrOp.py \"C:\Program Files\Reminder\"')
## Uninstaller.exe
print("Copying Uninstaller.exe...")
os.system('copy Uninstaller.exe \"C:\Program Files\Reminder\"')
## UninstallOp.exe
print("Copying UninstallOp.exe...")
os.system('copy UninstallOp.exe \"C:\Program Files\Reminder\"')

os.chdir(remindPath)
os.system('attrib +s +h +r \"C:\\Program Files\\Reminder\\UninstallOp.exe\"')

os.system('cd \"C:\Program Files\Reminder\" && echo %HOMEPATH% > userPath.txt')

print("Installation Completed")
print("Press \'Enter\' to exit...")
i = input()

