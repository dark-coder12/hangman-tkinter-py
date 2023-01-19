from words import words_list

import random
import tkinter
from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase

totalTurns = 0

word = random.choice(words_list)

wordList = list(word)
checkedLetters= []

for i in range(len(wordList)):
    checkedLetters.append('-')

page = tkinter.Tk()
page.title('Hang Man!')
page.config(bg = '#f2bc94')
width = page.winfo_screenwidth()
height = page.winfo_screenheight()
page.geometry("%dx%d" % (width, height))
page.bind("<Escape>", lambda event:page.destroy())
    
hang = [PhotoImage(file = "hang0.png"), PhotoImage(file = "hang1.png"), PhotoImage(file = "hang2.png")
              ,PhotoImage(file = "hang3.png"),PhotoImage(file = "hang4.png"),PhotoImage(file = "hang5.png")
              ,PhotoImage(file = "hang6.png"),PhotoImage(file = "hang7.png"),PhotoImage(file = "hang8.png"),
              PhotoImage(file = "hang9.png"),PhotoImage(file = "hang10.png"),PhotoImage(file ="hang11.png")]


#img = Label(page, image = hang[0])
#img.grid(row = 1 )


img = Label(page)
img.grid(row = 0, column = 0, rowspan = 3, columnspan = 3, padx = 10, pady = 40)
img.config(image = hang[0])

showLtr = StringVar()

Label(page, textvariable = showLtr, font= ("Courier", 20, "bold"), fg = "#f2bc94", bg="#30110d").grid(row = 0, column = 3, rowspan = 5, columnspan = 6, padx = 10)
n = 0

for alpha in ascii_lowercase:
    Button(page, text = alpha, command = lambda alpha=alpha :UserTurn(alpha), font = ("Courier", 20, "bold"), fg = '#f2bc94', bg = "#30110d").grid(row = 5+n//9, column = n%9, padx = 10, pady = 10)
    n+=1

showLtr.set(checkedLetters)
img.config(image = hang[0])


def UserTurn(letter):
   global totalTurns
   if(totalTurns < 11):
        
        if(letter in wordList):
           
            if(letter in checkedLetters):
                messagebox.showinfo("Hangman", "You've already guessed this letter!")
            else:
                for i in range(len(wordList)):
                    if(wordList[i] == letter):
                        checkedLetters[i] = letter
               
                showLtr.set(checkedLetters)
                print(showLtr.get())

            delimiter = '-'
            if(delimiter not in checkedLetters):
                messagebox.showinfo("Hangman", "You won!")
                return

        else:
            print(totalTurns)
            totalTurns+=1
            img.config(image = hang[totalTurns])

        if(totalTurns == 10):

                messagebox.showinfo("Hangman", "Game Over!")
                return


page.mainloop()