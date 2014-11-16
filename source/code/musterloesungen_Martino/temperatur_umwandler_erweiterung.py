#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

# Wir definieren die Konstanten, die wir brauchen, um die Temperaturen umzurechnen.
# Konvention: normalerweise werden die Namen von Konstanten mit Grossbuschstaben geschrieben.
ABSOLUTER_NP_K = 0.0      # absoluter Nullpunkt in Kelvin
ABSOLUTER_NP_C = -273.15  # absoluter Nullpunkt in Celsius
ABSOLUTER_NP_F = -459.67  # absoluter Nullpunkt in Fahrenheit

NULL_F = 32.0             # 0° C in Fahrenheit
FAKTOR_F_C = 9/5          # Umrechnungsfaktor zwischen Fahrenheit und Celsius

FEHLERMELDUNG_TEMP = "*** Fehler: unmögliche Temperatur! ***"  # Fehlermeldung für ungültige Eingabe

def get_float(msg = "Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")            
            
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

print()
print("*----------------------*")
print("* Temperatur Umwandler *")
print("*----------------------*")

wahl = -1
while wahl != 0:
    print()
    print("(1) Umrechnung von Celsius nach Kelvin")
    print("(2) Umrechnung von Celsius nach Fahrenheit")
    print("(3) Umrechnung von Kelvin nach Celsius")
    print("(4) Umrechnung von Kelvin nach Fahrenheit")
    print("(5) Umrechnung von Fahrenheit nach Celsius")
    print("(6) Umrechnung von Fahrenheit nach Kelvin")
    print()
    print("(0) Programm schliessen")
    print()
    print()
    wahl = int(input("Bitte wählen: "))
    print()
    if wahl == 1:
        t = get_float("Temperatur in Celsius: ")
        print(t, "° = ", Celsius_Kelvin(t), "K", sep = "")
    elif wahl == 2:
        t = get_float("Temperatur in Celsius: ")
        print(t, "° = ", Celsius_Fahrenheit(t), "F", sep = "")  
    elif wahl == 3:
        t = get_float("Temperatur in Kelvin: ")
        print(t, "K = ", Kelvin_Celsius(t), "°", sep = "")      
    elif wahl == 4:
        t = get_float("Temperatur in Kelvin: ")
        print(t, "K = ", Kelvin_Fahrenheit(t), "F", sep = "")   
    elif wahl == 5:
        t = get_float("Temperatur in Fahrenheit: ") 
        print(t, "F = ", Fahrenheit_Celsius(t), "°", sep = "") 
    elif wahl == 6:
        t = get_float("Temperatur in Fahrenheit: ") 
        print(t, "F = ", Fahrenheit_Kelvin(t), "K", sep = "") 
    else:
        print("Programm wird vom Benutzer beendet.")
        break