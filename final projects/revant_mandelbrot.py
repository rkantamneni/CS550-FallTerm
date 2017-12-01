#Fractals Project
#Revant Kantamneni  October 30, 2017
#I used two fucntions (incorporating recursivness) and the tkinter library to create three fractals from the Mandelbrot Set.

# import the libraries you'll need
import tkinter
from tkinter import *
import math
import colorsys # Tried using colorsys but it didn't work out
WIDTH = 300 # width and height of our picture in pixels
HEIGHT = 300
maxIt = 255 # max iterations; corresponds to color

#Setup for each window which is going to be used to display the fractals
window1 = Tk()#Root window
canvas1 = Canvas(window1, width = WIDTH, height = HEIGHT, bg = "#000000")#background color
img1 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas1.create_image((0, 0), image = img1, state = "normal", anchor = tkinter.NW)

window2 = Toplevel()#Sub Window
canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")#background color
img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)

window3 = Toplevel()
canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")#background color
img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)

#Mandelbrot calculation using the values coming in from the threeman function
def mandelbrot(z, c, count):
	z = (z**2)+c
	count+=1
	if abs(z)>2 or count>maxIt-1:
		return count
	return mandelbrot(z, c, count)

#Main function which manipulates the zooms and colors of the fractals, uses recursion
def threeman(xmin, xmax, ymin, ymax, rd1, rd2, gr1, gr2, bl1, bl2, win):

	global img1, img2, img3 #Variable Declaration
	
	# loop through all the pixels in the image
	for row in range(HEIGHT):
		for col in range(WIDTH):
			# calculate C for each pixel
			c = complex((((xmax-xmin)*col)/WIDTH)+xmin, (((ymax-ymin)*row)/HEIGHT)+ymin) #
			# set z to 0
			z = complex(0.0, 0.0)

			# execute the mandelbrot calculation
			r = mandelbrot(z, c, 0)
			#r = mandelbrot(z, c, 0)/255
			#rd=colorsys.hsv_to_rgb(r[0], s, v)
			#gr=colorsys.hsv_to_rgb(r[1], s, v)
			#bl=colorsys.hsv_to_rgb(r[2], s, v)
			# use the mandelbrot result to create a color
			rd = hex((r%(rd1))*rd2)[2:].zfill(2)#Red
			gr = hex((r%(gr1))*gr2)[2:].zfill(2)#Green
			bl = hex((r%(bl1))*bl2)[2:].zfill(2)#Blue

			if win==1:
				img1.put("#" + rd + gr + bl, (col, row))
			if win==2:
				img2.put("#" + rd + gr + bl, (col, row))
			if win==3:
				img3.put("#" + rd + gr + bl, (col, row))


#Calling on threeman function with the needed zoom and color values	 	
threeman(-0.7633854,-0.761927083, 0.088593750, 0.0900520833, 10, 10, 15, 17, 10, 10, 1)
threeman(0.290442426, 0.2909293384, -0.0142342194, -0.013747307219, 4, 64, 8, 32, 16, 16, 2)
#threeman(-0.74529, -0.74525, 0.113075, 0.11307, 4, 64, 8, 32, 16, 16, 3)
##threeman(-0.54133953060, -0.5405210, 0.61465970, 0.6154791430, 8, 16, 9, 20, 4, 64, 3)
threeman(-0.54133953060, -0.5405210, 0.61465970, 0.6154791430, 2, 20, 4, 40, 5, 60, 3)
canvas1.pack()#Sizes window 
canvas2.pack()
canvas3.pack()
mainloop()#Outputs everything

