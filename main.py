from tkinter import *

from tkinter import filedialog

window = Tk()

window.title("Pokemon")




window.geometry('400x230')

lbl = Label(window, text="Choose a Starter")

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="You Chose the Starter Charmander")

btn = Button(window, text="Charmander", bg="red",command=clicked)

btn.grid(column=1, row=0)







lbl = Label(window, text="Choose a Starter")

lbl.grid(column=0, row=2)

def clicked():

    lbl.configure(text="You Chose the Starter Squirtle")

btn = Button(window, text="Squirtle", bg="blue", command=clicked)

btn.grid(column=1, row=2)







lbl = Label(window, text="Choose a Starter")

lbl.grid(column=0, row=3)

def clicked():

    lbl.configure(text="You Chose the Starter Bulbasaur")

btn = Button(window, text="Bulbasaur", bg="green",command=clicked)

btn.grid(column=1, row=3)



lbl = Label(window, text="Edward Testing / First GUI")

lbl.grid(column=0, row=6)

lbl = Label(window, text="Started in 2022")

lbl.grid(column=0, row=7)




window.mainloop()




