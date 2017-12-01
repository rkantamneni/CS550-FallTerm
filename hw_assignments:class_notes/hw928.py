'''
for i in range(1000,2001):
	print(i, end=' ')

	if (i+1)%5==0:
    	 print(i)

#It creates the fibonacci sequence
'''
import random
number = int(input("Number of times to flip coin: "))
heads = 0
for amount in range(number):
    flip = random.randint(0, 1)
    if (flip == 0):
              heads = heads+1
percent = (heads/number)*100
print('The coin flipped to heads is '+ str(percent)+'%')
#It's always going to be 50% if the amount of flips is even. True randomness can't be acheived
   