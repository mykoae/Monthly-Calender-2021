def Calender_2021():
    print("MONTHLY CALENDER FOR YEAR 2021")

Calender_2021()
print("Type and enter first three letters of the month in lowercase or type full month with uppercase first letter...")

MonthNumbers = {
"jan" : "January",
"feb" : "February",
"mar" : "March",
"apr" : "April",
"may" : "May",
"jun" : "June",
"jul" : "July",
"aug" : "August",
"sep" : "September",
"oct" : "October",
"nov" : "November",
"dec" : "December",
}

import calendar

print("e.g jan or January?")

MonthNumbers = (input("Type a Month in 2021?: "))

if MonthNumbers == "jan" or MonthNumbers == "January":
    print(calendar.month(2021,1))
if MonthNumbers == "feb" or MonthNumbers == "Febuary":
    print(calendar.month(2021,2))
if MonthNumbers == "mar" or MonthNumbers == "March":
    print(calendar.month(2021,3))
if MonthNumbers == "apr" or MonthNumbers == "April":
    print(calendar.month(2021,4))
if MonthNumbers == "may" or MonthNumbers == "May":
    print(calendar.month(2021,5))
if MonthNumbers == "jun" or MonthNumbers == "June":
    print(calendar.month(2021,6))
if MonthNumbers == "jul" or MonthNumbers == "July":
    print(calendar.month(2021,7))
if MonthNumbers == "aug" or MonthNumbers == "August":
    print(calendar.month(2021,8))
if MonthNumbers == "sep" or MonthNumbers == "September":
    print(calendar.month(2021,9))
if MonthNumbers == "oct" or MonthNumbers == "October":
    print(calendar.month(2021,10))
if MonthNumbers == "nov" or MonthNumbers == "November":
    print(calendar.month(2021,11))
if MonthNumbers == "dec" or MonthNumbers == "December":
    print(calendar.month(2021,12))
