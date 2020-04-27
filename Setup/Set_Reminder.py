import datetime
import time
import sys
import os

import StrOp

newUserPath=''
with open('userPath.txt', 'rt') as f:
    userPath = f.read()
for i in range(1, len(userPath)-2):
    newUserPath+=userPath[i]
dateLocation = 'C:\\' + newUserPath + '\\Documents\\Reminder'

def SetOp():
    dateSave = input("Please give me a date that you want me to remind (format: dd-mm-yyyy): ")

    ## Kiểm tra coi format đúng không
    if not StrOp.CheckDateFormat(dateSave):
        print("Wrong date format!!!")
        print("Exiting...")
        time.sleep(3)
        sys.exit()

    ## Kiểm tra coi ngày hợp lệ hay không
    if not StrOp.DayValid(dateSave):
        print("No day valid!!!")
        print("Exiting...")
        time.sleep(3)
        sys.exit()

    ## Kiểm tra coi ngày  ở tương lai hay không
    if not StrOp.FutureDate(dateSave):
        print('It\'s the past')
        print("Exiting...")
        time.sleep(3)
        sys.exit()

    ## Tạo file name
    fileName = StrOp.CorrectDate(dateSave) + '.txt'

    title = input("Enter the title: ")
    content = input("Enter the content: ")
    note = input("Notes: ")
    deadline = input("Deadline: ")

    ## Kiểm tra coi thư mục lưu trữ đã tạo chưa, chưa thì tạo
    if os.path.exists(dateLocation):
        os.chdir(dateLocation)
    else:
        os.mkdir(dateLocation)
        os.chdir(dateLocation)

    ## Kiểm tra coi có bị trùng ngày ghi chú không, không trùng sẽ write new,
    ## trùng sẽ append
    if os.path.exists(fileName):
        with open(fileName, 'at') as f:
            f.write("\n\n--------------------------------------------------\n")
            f.write('\n\nTitle: ' + title + '\n\n')
            f.write(content + '\n')
            if not note=='':
                f.write('Notes: ' + note + '\n')
            if not deadline=='':
                f.write('Deadline: ' + deadline + '\n')
    else:
        with open(fileName, 'wt') as f:
            f.write('Title: ' + title + '\n\n')
            f.write(content + '\n')
            if not note=='':
                f.write('Notes: ' + note + '\n')
            if not deadline=='':
                f.write('Deadline: ' + deadline + '\n')
                
if __name__ == '__main__':
    while True:
        print("Welcome to 'Set Reminder'!!!")
        print("1. See your saved reminder    2. Create new reminder    3. Quit")
        i = input("Your answer: ")
        if i=='1':
            os.system(f'cd C:\{newUserPath}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup && start Reminder.exe')
            print("Opening your reminder...")
            time.sleep(5)
            os.system('cls')
        elif i=='2':
            SetOp()
            os.system('cls')
        elif i=='3':
            break
        else:
            print('Wrong answer!!!')
            os.system('cls')
