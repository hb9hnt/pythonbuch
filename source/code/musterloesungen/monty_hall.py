#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

from tkinter import *
from random import randint

# given a door (n=0,1 or 2) this functions indicate a goat which is hidden behind another door.
def indicate_goat(n):
    if prizes[n]:
        goat = randint(1,2)
        message((n+goat)%3)
    else:
        if prizes[(n+1)%3]:
            message((n+2)%3)
        else:
            message((n+1)%3)

# action if the door A is chosen
def doorA_action():
    global step
    if step == 0: # first choice
        indicate_goat(0)
        step += 1
        doorA.configure(background="red")
    else: # second choice (after one goat is shown
        result(0)
        if prizes[0]:
            doorA.configure(image=fiat500, state=DISABLED,background="red")
            doorB.configure(image=goat, state=DISABLED,background="gray")
            doorC.configure(image=goat, state=DISABLED,background="gray")
        else:
            doorA.configure(image=goat, state=DISABLED,background="red")
            if prizes[1]:
                doorB.configure(image=fiat500, state=DISABLED,background="gray")
            else:
                doorC.configure(image=fiat500, state=DISABLED,background="gray")

# action if the door B is chosen
def doorB_action():
    global step
    if step == 0:
        indicate_goat(1)
        step += 1
        doorB.configure(background="red")
    else:
        result(1)
        if prizes[1]:
            doorB.configure(image=fiat500, state=DISABLED,background="red")
            doorA.configure(image=goat, state=DISABLED,background="gray")
            doorC.configure(image=goat, state=DISABLED,background="gray")
        else:
            doorB.configure(image=goat, state=DISABLED,background="red")
            if prizes[0]:
                doorA.configure(image=fiat500, state=DISABLED,background="gray")
            else:
                doorC.configure(image=fiat500, state=DISABLED,background="gray")

# action if the door C is chosen
def doorC_action():
    global step
    if step == 0:
        indicate_goat(2)
        step += 1
        doorC.configure(background="red")
    else:
        result(2)
        if prizes[2]:
            doorC.configure(image=fiat500, state=DISABLED,background="red")
            doorA.configure(image=goat, state=DISABLED,background="gray")
            doorB.configure(image=goat, state=DISABLED,background="gray")
        else:
            doorC.configure(image=goat, state=DISABLED,background="red")
            if prizes[0]:
                doorA.configure(image=fiat500, state=DISABLED,background="gray")
            else:
                doorB.configure(image=fiat500, state=DISABLED,background="gray")

# this function modifies the message at the bottom of the window after the first choice
def message(n):
    if n == 0:
        s = "A"
    elif n == 1:
        s = "B"
    else:
        s = "C"
    
    communication = "Behind door " + s + " there is a goat! \nDo you want to change door?"
    message2.config(text = communication)
    if s == "A":
        doorA.configure(image=goat, state=DISABLED)
    elif s == "B":
        doorB.configure(image=goat, state=DISABLED)
    else:
        doorC.configure(image=goat, state=DISABLED)

# this function modifies the message at the bottom of the window after the second choice
def result(n):
    if prizes[n]:
        s = "CONGRATULATION! YOU WON A CAR!"
    else:
        s = "Sadly you only won a goat..."
    message2.configure(text=s)

def start_new_game():
    global prizes # IMPORTANT: this variable is global
    prizes = [False,False,False]
    car = randint(0,2)
    prizes[car] = True
    global step # IMPORTANT: this variable is global
    step = 0
    doorA.configure(state=NORMAL,image=door,background="gray")
    doorB.configure(state=NORMAL,image=door,background="gray")
    doorC.configure(state=NORMAL,image=door,background="gray")
    start_game.configure(text="New Game")
    message2.configure(text="Please pick a door!")
        
fenster = Tk()
fenster.title("Monty Hall Problem")

# load images
goat=PhotoImage(file="Boer-Goat.gif")
door=PhotoImage(file="door.gif")
fiat500=PhotoImage(file="fiat500.gif")

message1 = Label(fenster, height = 5, font=("Helvetica", 16),
                 text="Welcome to our game! \nBehind one of these doors there is a car. \nBehind the other two, goats!")
message2 = Label(fenster, height = 5, text = "", font=("Helvetica", 16))

start_game = Button(fenster, font=("Helvetica", 16),
                    text="Click here to \nstart the game",
                    command=start_new_game, activebackground = "yellow")

doorA = Button(fenster, image=door, font=("Helvetica", 16),
               text = "Door A", state=DISABLED, compound="bottom",
               command=doorA_action, activebackground = "yellow")
doorB = Button(fenster, image=door, font=("Helvetica", 16),
               text = "Door B", state=DISABLED, compound="bottom",
               command=doorB_action, activebackground = "yellow")
doorC = Button(fenster, image=door, font=("Helvetica", 16),
               text = "Door C", state=DISABLED, compound="bottom",
               command=doorC_action, activebackground = "yellow")

message1.grid(row=0, columnspan=2, sticky=W+E+N+S, pady=20)
start_game.grid(row=0, column=2, pady=20)
doorA.grid(row=1,column=0,pady=20, padx=20)
doorB.grid(row=1,column=1,pady=20, padx=20)
doorC.grid(row=1,column=2,pady=20, padx=20)
message2.grid(row=2, columnspan=3, sticky=W+E+N+S, pady=20)
 
menubar = Menu(fenster)

game_menu = Menu(menubar, tearoff=0)

game_menu.add_command(label="New Game", command=start_new_game)
game_menu.add_separator()
game_menu.add_command(label="Quit", command=fenster.quit)

menubar.add_cascade(label="Game", menu=game_menu)

fenster.config(menu=menubar)          

fenster.mainloop()