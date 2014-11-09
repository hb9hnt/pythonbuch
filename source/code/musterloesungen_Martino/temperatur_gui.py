#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

from tkinter import *

ABSOLUTER_NP_K = 0.0      # absoluter Nullpunkt in Kelvin
ABSOLUTER_NP_C = -273.15  # absoluter Nullpunkt in Celsius
ABSOLUTER_NP_F = -459.67  # absoluter Nullpunkt in Fahrenheit

NULL_F = 32.0             # 0° C in Fahrenheit
FAKTOR_F_C = 9/5          # Umrechnungsfaktor zwischen Fahrenheit und Celsius

FEHLERMELDUNG_TEMP = "*** Fehler: unmögliche Temperatur! ***"  # Fehlermeldung für ungültige Eingabe

def button_action():
    temperatur_str = eingabefeld.get()
    temperatur = float(temperatur_str)
    wahl = variable.get()
    if wahl == u1:
        message = temperatur_str + "° = " + str(Celsius_Kelvin(temperatur)) + "K"
    elif wahl == u2:
        message = temperatur_str + "° = " + str(Celsius_Fahrenheit(temperatur)) + "F"
    elif wahl == u3:
        message = temperatur_str + "K = " + str(Kelvin_Celsius(temperatur)) + "°"
    elif wahl == u4:
        message = temperatur_str + "K = " + str(Kelvin_Fahrenheit(temperatur)) + "F"
    elif wahl == u5: 
        message = temperatur_str + "F = " + str(Fahrenheit_Celsius(temperatur)) + "°"
    elif wahl == u6: 
        message = "F = " + str(Fahrenheit_Kelvin(temperatur)) + "K"  
    ausgabe.configure(text=message)

def Celsius_Kelvin(t):
    if t >= ABSOLUTER_NP_C:
        return t - ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP) 

def Celsius_Fahrenheit(t):
    if t >= ABSOLUTER_NP_C:
        return NULL_F + FAKTOR_F_C*t
    else:
        raise TypeError(FEHLERMELDUNG_TEMP) 
            
def Kelvin_Celsius(t):
    if t >= ABSOLUTER_NP_K:
        return t + ABSOLUTER_NP_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP) 
        
def Kelvin_Fahrenheit(t):
    if t >= ABSOLUTER_NP_K:
        return t*FAKTOR_F_C + ABSOLUTER_NP_F 
    else:
        raise TypeError(FEHLERMELDUNG_TEMP) 

def Fahrenheit_Celsius(t):
    if t >= ABSOLUTER_NP_F:
        return (t - NULL_F)/FAKTOR_F_C 
    else:
        raise TypeError(FEHLERMELDUNG_TEMP) 
        
def Fahrenheit_Kelvin(t):
    if t >= ABSOLUTER_NP_F:
        return (t - ABSOLUTER_NP_F)/FAKTOR_F_C
    else:
        raise TypeError(FEHLERMELDUNG_TEMP)

fenster = Tk()
fenster.title("Temperatur Umwandler")

info = Label(fenster, justify = LEFT, font=("Helvetica", 16),
             text="""\
************* TEMPERATUR UMWANDLER *************
       1) Gewünschte Umrechnung wählen.
       2) Temperatur eingeben.
       3) Taste "Umrechnen" dränglen.""")

u1 = "von Celsius nach Kelvin"
u2 = "von Celsius nach Fahrenheit"
u3 = "von Kelvin nach Celsius"
u4 = "von Kelvin nach Fahrenheit"
u5 = "von Fahrenheit nach Celsius"
u6 = "von Fahrenheit nach Kelvin"

variable = StringVar(fenster)
variable.set(u1) # default value

optionen = OptionMenu(fenster, variable, u1, u2, u3, u4, u5, u6)
optionen.configure(width = 40, font=("Helvetica", 16))
eingabefeld = Entry(fenster, bd=5, width=20)
label = Label(fenster, justify = LEFT, font=("Helvetica", 16), text="Ausgabe: ")
ausgabe = Label(fenster, justify = CENTER, font=("Helvetica", 16), text=" ")
run_button = Button(fenster,text="Umrechnen", font=("Helvetica", 16), command = button_action)

info.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 50)
optionen.grid(row = 1, column = 0, columnspan = 3, pady = 20)
eingabefeld.grid(row = 2, column = 0, pady = 20)
run_button.grid(row = 2, column = 1, pady = 20)
label.grid(row = 3, column = 0, pady = 20)
ausgabe.grid(row = 3, column = 1, columnspan = 2, pady = 20)

fenster.mainloop()