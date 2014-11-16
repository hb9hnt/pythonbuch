#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

print("\n===========================================")
print("# Professor Ungerechtmann, KS Unfairdorf #")
print("===========================================\n")

pruefungsnote = float(input("Prüfungsnote (von 1 bis 6 mit Halbpunkten): "))
if (pruefungsnote*10) % 5 == 0 and pruefungsnote >= 1 and pruefungsnote <= 6:  # gültige Eigabewert für die Prüfungsnote
    augenfarbe = int(input("Augenfarbe des Prüflings (1=dunkel, 0=hell): "))
    if augenfarbe == 1 or augenfarbe == 0: # gültige Eigabewert für die Augenfarbe
        frisur = int(input("Frisur des Prüflings (1=kurze Haare, 0=lange Haare): "))
        if frisur == 1 or frisur == 0: # gültige Eigabewert für die Frisur
            if augenfarbe == 1:
                if frisur == 1:
                    abschlussnote = pruefungsnote + 0.1*pruefungsnote
                else:
                    abschlussnote = pruefungsnote - 0.1*pruefungsnote 
            else:
                if frisur == 1:
                    abschlussnote = pruefungsnote - 0.1*pruefungsnote
                else:
                    abschlussnote = pruefungsnote + 0.1*pruefungsnote
            wetter = int(input("Wetter: (1=schön, 0=nicht schön): "))
            if wetter == 1 or wetter == 0: # gültige Eigabewert für das Wetter
                if wetter == 1:
                    abschlussnote = abschlussnote - 1
            else:
                print("Fehler: ungültiger Eingabewert für das Wetter!")        
                
            if abschlussnote > 6.0:
                abschlussnote = 6.0
            elif abschlussnote < 1.0:
                abschlussnote = 1.0
            else:
                abschlussnote = round(2.0*abschlussnote)/2                  
            print("\nAbschlussnote:", abschlussnote)
        else:
            print("Fehler: ungültiger Eingabewert für die Frisur!") 
    else:
        print("Fehler: ungültiger Eingabewert für die Augenfarbe!")
else:
    print("Fehler: ungültige Prüfungsnote!")