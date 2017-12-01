
import sys
import random
for x in range(1):
  orig=random.randint(1,10)
again='y'

while again=='y':
	num = int(input('Write a number between 1 and 10: '))
	if num==orig:
		print('You guessed correct')
	else:
		print('You guessed incorrect')
		if num>orig:
			print('Too high')
		elif num<orig:
			print('Too low')
	again = input('Want to play again? (y/n)')
print('Thanks for playing.')




'''
import sys

num = int(input('How fast were you going?: '))
birth = input('Is today your birthday (y/n): ')
if birth=='y':
	num=num-5
if num<60:
	print('No ticket')
elif num<80 and num>60:
	print('Small ticket')
elif num>80:
	print('Big ticket')

'''