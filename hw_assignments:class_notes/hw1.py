import sys

# What does end='' do in the print statements?
# Respond here:  The end='' makes sure console doesn't move on to the next line.
print('Hello ', end='')
print(sys.argv[1], end=', ')
print(sys.argv[2], end=', and ')
print(sys.argv[3], end='')
print('! Welcome.')
# To run this code: 
#You need to enter the directory with cd and then drag and drop the folder directory
#Then you type python3 filename.py Arguments. If you have arguments, put them 
#after the file name.
