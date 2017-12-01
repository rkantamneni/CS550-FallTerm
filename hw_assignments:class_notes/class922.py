import time
import sys

print('Welcome to your very own Adventure story!')
n = input ('What is your name?')
print('Well, hello there '+n)
time.sleep(2)
print('Would you like to be the king of Camelot?')
a = str(input("Answer: "))
if a=="yes":
	print('Okay then')
elif a=="no":
	print('')

