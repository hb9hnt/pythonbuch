# Tkinter ist ein Paket zum erstellen von GUIs
from tkinter import *

# Funktion, welche beim Klick des Buttons
# ausgeführt wird.
def action():
    print("Aua!")

# Ein Fenster erstellen
fenster = Tk()

# Einen Button erstellen
button = Button(fenster, text="Hit me!", command=action)
button.pack()

mainloop()
