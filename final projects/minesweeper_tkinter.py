#Minesweeper by Revant Kantamneni
#November 16, 2001
#I created a game of minesweeper using all the things we learnt this term.
#I spent a large amount of time toying with tkinter and recursion to get this to work.
#I was able to practice using classes through this project
from tkinter import *
from functools import partial
from random import randint
import time

class Game: #Created a class for the primary reason of creating the user interface
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.root = Tk() #Setup for root window
        self.board_rowcol=10 #Creates a 10x10 Minesweeper board
        self.label = Label(master, text="Welcome to Minesweeper by Revant Kantamneni")
        self.label.pack()
       # self.label2.pack() Need box syntax
        self.row = -1
        self.col = -1
        self.board=[] #Empty board array
        self.mines=[] #Empty mines array
        self.near=0 #Variable to be used to see if there is a mine nearby
        self.wrong=0
        self.frame1 = Frame(self.root, width = 900, height = 30) #Window size for tkinter window
        self.frame1.grid()
        self.case=False
        self.makeminesboard() #Calls on function to make mines coordinates. 
        self.display() #Creates grid of buttons with mines and numbers
        # self.play()#Calls main function which plays
        
        self.root.mainloop() #setup window


    def makeminesboard(self):
        for i in range(self.board_rowcol): #Inputs X into all buttons
            self.board.append(["X"]*self.board_rowcol)
        for i in range(15): #Overwrites X coordinates with mine coordinates
            self.mines.append([randint(0, self.board_rowcol-1), randint(0, self.board_rowcol-1)])
        self.mines.append([0,0])

    def display(self): #Setup for GUI window 10x10 window
        for r in range(self.board_rowcol):
            for c in range(self.board_rowcol):
                button = Button(self.frame1, text=str(self.board[r][c]), width = 2,
                                height = 2, padx = 20, pady = 5, command =partial(self.play, r, c))#This is how you create a button.
                               
                ## the label is in the top row so add one to each row
                button.grid(row=r, column=c)
    

    def near_mines(self,r, c, near): #Code to see if there is a mine near the selected coordinate and the vairable near gets anumner which gets displayed on the board
        self.near=0
        if [r+1, c] in self.mines:
            self.near+=1
        if [r+1, c+1] in self.mines:
            self.near+=1
        if [r, c+1] in self.mines:
            self.near+=1
        if [r-1, c+1] in self.mines:
            self.near+=1
        if [r-1, c] in self.mines:
            self.near+=1
        if [r-1, c-1] in self.mines:
            self.near+=1
        if [r, c-1] in self.mines:
            self.near+=1
        if [r+1, c-1] in self.mines:
            self.near+=1
        return self.near

    def game_over(self): #Code to end game and exit out
        self.wrong=1
        print('You clicked a mine! Game over!')
        self.label = Label(text="You clicked a mine! Game over!")
        self.label.pack()
        mainloop()
        time.sleep(3)
        exit()

    def surround(self, r, c): #If there is a zero, it reveals the surrounding cells. If those cells have zeros, it revels the ones around them. I used recursion and this took 2.5 hours to figure out.

        if self.board[r][c]== "0": #If there is a zero in the place run the code.
            #Following check around the zero and give them values. I got recusion erros and fixed that by putting an "and coordinate==X"
            if r < self.board_rowcol-1 and self.board[r+1][c]=="X":
                self.board[r+1][c] = str(self.near_mines(r+1, c, 0))
                self.surround(r+1, c)

            if r < self.board_rowcol-1 and c < self.board_rowcol-1 and self.board[r+1][c+1]=="X":
                self.board[r+1][c+1] = str(self.near_mines(r+1, c+1, 0))
                self.surround(r+1, c+1)

            if c < self.board_rowcol-1 and self.board[r][c+1]=="X":
                self.board[r][c+1] = str(self.near_mines(r, c+1, 0))
                self.surround(r, c+1)

            if r > 0 and c < self.board_rowcol-1 and self.board[r-1][c+1]=="X":
                self.board[r-1][c+1] = str(self.near_mines(r-1, c+1, 0))
                self.surround(r-1, c+1)
                    

            if r > 0 and self.board[r-1][c]=="X":
                self.board[r-1][c] = str(self.near_mines(r-1, c, 0))
                self.surround(r-1, c)
                    

            if r > 0 and c > 0 and self.board[r-1][c-1]=="X":
                self.board[r-1][c-1] = str(self.near_mines(r-1, c-1, 0))
                self.surround(r-1, c-1)
                    

            if c > 0 and self.board[r][c-1]=="X":
                self.board[r][c-1] = str(self.near_mines(r, c-1, 0))
                self.surround(r, c-1)


            if r < self.board_rowcol-1 and c > 0 and self.board[r+1][c-1]=="X": 
                self.board[r+1][c-1] = str(self.near_mines(r+1, c-1, 0))
                self.surround(r+1, c-1)


    def play(self, r1, c1): #Play function: When a cell is clicked, this function is run. 
        self.case=True
        if self.wrong==0:
            while self.case==True:
                if [r1, c1] in self.mines:
                    self.case=False
                    print(self.case)
                    self.game_over()
                else:
                    self.board[r1][c1] = str(self.near_mines(r1, c1, 0)) #Set cell value to how many surroudning mines there are to the cell's cooridnate
                    self.surround(r1, c1)
                    self.display()
                    self.case=False
            self.display()

app = Game(Tk())

