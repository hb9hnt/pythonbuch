#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

print()
print("*-------------------------------*")
print("* Steueramt Flächenlandrepublik *")
print("*-------------------------------*")
print()

GRENZE_1 = 10000.0
GRENZE_2 = 30000.0
GRENZE_3 = 70000.0
STEUERSATZ_1 = 0.40  # 40%
STEUERSATZ_2 = 0.55  # 55%
STEUERSATZ_3 = 0.75  # 75%
STEUERSATZ_4 = 0.82  # 82%

nachname = input("Nachname des Steuerzahlers: ")
vorname = input("Vorname des Steuerzahlers: ")

einkommen = 0.0
while einkommen <= 0.0:
    einkommen = float(input("Einkommen (in Dublonen): "))
    if einkommen <= 0.0:
        print("Eingabe nicht gültig! Bitte nochmals das Einkommen eingeben: ")

steuer = 0.0
if einkommen <= GRENZE_1:
    steuer = einkommen * STEUERSATZ_1
elif einkommen <= GRENZE_2:
    steuer = einkommen * STEUERSATZ_2
elif einkommen <= GRENZE_3:
    steuer = einkommen * STEUERSATZ_3
else:
    steuer = einkommen * STEUERSATZ_4    
                
print("Der Steuerzahler " + nachname + " " + vorname + " muss für das laufende Jahr", round(steuer), "Dublonen dem Steueramt bezahlen.")               