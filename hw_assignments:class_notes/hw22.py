import sys
import math

m = int(input ('Type in a month value between 1-12: '))
d = int(input ('Type in a day value between 1-31: '))
y = int(input ('Type in a year value: '))

month = ((m + 12) * ((14 - m) // 12)) - 2
year = y - (14 - m) // 12
x = year + year//4 - year//100 + year//400
day = int((d + x + (31*m) // 12) % 7)

if (day==0):print('Sunday')
if (day==1):print('Monday')
if (day==2):print('Tuesday')
if (day==3):print('Wednesday')
if (day==4):print('Thursday')
if (day==5):print('Friday')
if (day==6):print('Saturday')
print (month)
print(day)