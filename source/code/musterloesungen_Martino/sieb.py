#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

from math import sqrt

def sieb(n):
    L = [True]*n
    L[0] = L[1] = False        # 0, 1 sind keine Primzahlen
    sqrtN = int(sqrt(n))       # Grenze für die Suche
    i = 2
    while i <= sqrtN:
        if L[i]:               # L[i] muss True sein
            for j in range(2*i, n, i):
                L[j] = False
        i = i + 1
    return L

def main():
    n = int(input("Bitte eine natürliche Zahl eingeben: "))
    n = n + 1
    L = sieb(n)
    zaehler = 0
    for i in range(n):
        if L[i]:
            zaehler = zaehler + 1
            print(i, end = "\t")
            if zaehler % 8 == 0: # layout: jede achte Primzahl -> Zeilenvorschub
                print()
    print()
    print("Es gibt", zaehler, "Primzahlen <=", n-1);
    
main()
