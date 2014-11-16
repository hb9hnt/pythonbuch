from tkinter import *

fenster = Tk()

variable = StringVar(fenster)
variable.set("one") # default value

w = OptionMenu(fenster, variable, "one", "two", "three")
w.pack()

fenster.mainloop()