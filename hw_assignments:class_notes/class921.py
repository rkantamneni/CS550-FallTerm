
import sys
import math

print('Hello, ', end='')
print(sys.argv[1], end='')
print('!')
response = input ('What is your favorite food? ')
print('Mmm!' + response+' are delicious!')
response = input ('What is your address? ')
print('Nice! I live in the neighborhood next to ' + response+'.')

#typecasting is changing types
#concatenation is combining strings
#abs, max, min, round, 
#2000 was a leap year
response = input ('Type in year:')
return int(response)
a=response%4==0
a=response%100==0
a=response%400==0



