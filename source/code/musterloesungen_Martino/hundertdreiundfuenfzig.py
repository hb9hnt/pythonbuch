#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

def quersumme_dritter_potenzen(N):
    summe = 0
    while N != 0:
        summe = summe + (N % 10)**3
        N = N // 10
    return summe

def durch_drei_teilbar(N):
    return N % 3 == 0

print()
print("*-----*")
print("* 153 *")
print("*-----*")
print()

N = int(input("Bitte eine positive ganze Zahl eingeben, die durch 3 teilbar ist: "))
while (not durch_drei_teilbar(N)):
    print("Fehler! " + str(N) + " ist nicht durch 3 teilbar.")
    N = int(input("Bitte eine andere Zahl wählen: "))

M = 0
print(N)
while M != N:
    M = N
    N = quersumme_dritter_potenzen(N)
    print(N)