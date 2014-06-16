from tkinter import *
from tkinter import messagebox

def button_action():
        print("Ich wurde über das Menü ausgeführt.")
        
def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Hans Mustermann\n\
Date: 16.06.14\n\
Version: 1.07\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
        
fenster = Tk()
fenster.title("Programm mit einem Menü")

info_text = Label(fenster, text = "Ich habe ein Menü!\n\
Wenn du darauf Klickst geht ein Drop-Down-Menü auf.")
info_text.pack()

# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menü Datei und Help erstellen
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="Anwenden", command=button_action)
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Exit", command=fenster.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
# "Drop-Down-Menü" hinzu
menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
fenster.config(menu=menuleiste)          

fenster.mainloop()
