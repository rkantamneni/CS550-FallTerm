import sys
import math
print ('Wind Chill Calculator')
t = int(input('What is the temperature? '))
v = float(input('What is the wind speed? '))

if t<50 and v<120 and v>3:
	w = 35.74 + (0.6215*t) + ((0.4275*t) - 35.75)*(v**0.16)
	print('The wind chill is '+ str(w))
else:
	print('Please enter a temperature that is less than 50 C and/or a wind speed less than 120 mph and more than 3 mph.')
