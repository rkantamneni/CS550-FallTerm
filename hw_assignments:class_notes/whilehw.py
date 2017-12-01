import sys
'''
x=1
while (x<11):
 	print (x)
 	x=x+1
'''

'''
x=56
while (x>29):
 	print (x)
 	x=x-2
'''

response = input ('What is black and white and read all over?: ')
while(response != 'newspaper'):
	print('Try again!')
	response = input ('What is black and white and read all over?')
if(response=='newspaper'):
	print('You got it correct!')

