#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")

wahl = input("Bitte wählen: ")

if wahl == "1":
    celsius = float(input("Temperatur in Celsius: "))
    if celsius >= -273.15:
        kelvin = celsius + 273.15
        print(celsius, "° = ", kelvin, "K", sep = "")
    else:
        print("Fehler: unmögliche Temperatur!")
elif wahl == "2":
    celsius = float(input("Temperatur in Celsius: "))
    if celsius >= -273.15:
        fahrenheit = 32.0 + 1.8*celsius
        print(celsius, "° = ", fahrenheit, "F", sep = "")    
    else:
        print("Fehler: unmögliche Temperatur!")   
elif wahl == "3":
    kelvin = float(input("Temperatur in Kelvin: "))
    if kelvin >= 0.0:
        celsius = kelvin - 273.15
        print(kelvin, "K = ", celsius, "°", sep = "") 
    else:
        print("Fehler: unmögliche Temperatur!")           
elif wahl == "4":
    kelvin = float(input("Temperatur in Kelvin: "))
    if kelvin >= 0.0:    
        fahrenheit = kelvin*1.8 - 459.67
        print(kelvin, "K = ", fahrenheit, "F", sep = "")  
    else:
        print("Fehler: unmögliche Temperatur!")       
elif wahl == "5":
    fahrenheit = float(input("Temperatur in Fahrenheit: "))    
    if fahrenheit >= -459.67:
        celsius = 5.0*(fahrenheit - 32.0)/9.0
        print(fahrenheit, "F = ", celsius, "°", sep = "")   
    else:
        print("Fehler: unmögliche Temperatur!")        
elif wahl == "6":
    fahrenheit = float(input("Temperatur in Fahrenheit: ")) 
    if fahrenheit >= -459.67:    
        kelvin = (fahrenheit + 459.67)/1.8
        print(fahrenheit, "F = ", kelvin, "K", sep = "")  
    else:
        print("Fehler: unmögliche Temperatur!")        
else:
    print("Falsche Eingabe!")    