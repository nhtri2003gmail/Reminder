import datetime
import time
import sys
import os

def DayMonthYear():
    now = str(datetime.datetime.now())
    today = now.split(' ')
    
    t = str(today[0])
    date = t.split('-')
    
    return date[2] + '-' + date[1] + '-' + date[0]

def CheckDateFormat(dateSave):
    try:
        date = dateSave.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
    except:
        return False    
    return True

def CorrectDate(dateSave):
    date = dateSave.split('-')
    day = str(date[0])
    month = str(date[1])
    year = str(date[2])
    if len(day)==1:
        day = '0' + day
    if len(month)==1:
        month = '0' + month
    newStr = day + '-' + month + '-' + year
    return newStr

def DayValid(dateSave):
    date = dateSave.split('-')
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    if year%4==0:
        if month==2:
            if day>29:
                return False
    else:
        if month==2:
            if day>28:
                return False

    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day>31:
            return False
    elif month==4 or month==6 or month==9 or month==11:
        if day>30:
            return False
    elif month>12:
        return False

    return True    

def FutureDate(dateSave):
    correctDate = CorrectDate(dateSave)
    today = DayMonthYear()

    dateNow = today.split('-')
    date = dateSave.split('-')

    dayNow = int(dateNow[0])
    monthNow = int(dateNow[1])
    yearNow = int(dateNow[2])
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    if year<yearNow:
        return False
    elif year==yearNow:
        if month<monthNow:
            return False
        else:
            if day<dayNow:
                return False
    
    return True








    
