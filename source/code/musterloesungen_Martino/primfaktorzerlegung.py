#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

from time import clock
from math import sqrt

def get_posint1(msg = "Bitte eine natürliche Zahl > 1 eingeben: "): 
    while True:
        try:
            eingabe = int(input(msg))
            return eingabe
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren...")

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
    liste_prim = []
    for j in range(n):
        if L[j]:
            liste_prim.append(j)
    return liste_prim

def trial_div(n):
    liste_faktoren = []
    exponent = 0
    
    sqrt_n = int(sqrt(n))
    liste_prim = sieb(sqrt_n)
    
    index = 0
    while index < len(liste_prim):
        d = liste_prim[index]
        exponent = 0
        while n % d == 0:
            exponent += 1
            n = n // d
        if exponent > 0:
            liste_faktoren.append([d, exponent])
        index += 1    
    
    if n != 1:
        liste_faktoren.append([n, 1])
    return liste_faktoren   


def pretty_print(n, L):
    """
    Diese Funktion druckt die Primfaktorzerlegung in dieser Form aus
      p1^e1 * p2^e2 * ... * pk^ek.
    """
    m = len(L) - 1
    print(n, "=", end = " ")
    for i in range(m):
        if L[i][1] != 1:
            print(str(L[i][0]) + "^" + str(L[i][1]), end = " * ")
        else:
            print(str(L[i][0]),  end = " * ")
    if L[m][1] != 1:
        print(str(L[m][0]) + "^" + str(L[m][1]))        
    else:
        print(str(L[m][0]))     
    
def main():
    print()
    print("***************************")
    print("*** Primfaktorzerlegung ***")
    print("***************************")
    print()
    n = get_posint1()
    print()

    start = clock()
    P = trial_div(n)
    stop = clock()

    lenP = len(P)
    if (lenP == 1) and (P[0][1] == 1):
        print(n, "ist eine Primzahl")
    else: 
        pretty_print(n, P)
    
        # Überprüfung
        produkt = 1
        for i in range(lenP):
            produkt = produkt * (P[i][0]**P[i][1])
        if produkt == n:
            print("\nÜberprüfung ok!\n")
        else:
            print("\nFehler!\n")
    
    # Berechnungszeit
    dt = stop - start
    print("\n*** Berechnungszeit: {0:>3.5f} s ***".format(dt))
    
main()