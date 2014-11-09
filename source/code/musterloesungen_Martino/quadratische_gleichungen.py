#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

# Quadratische Wurzel importieren
from math import sqrt

print("\nProgramm zur Lösung der quadratische Gleichung ax^2 + bx + c = 0")
print("========================================================================\n")
a = float(input('Koeffizient a: '))
b = float(input('Koeffizient b: '))
c = float(input('Koeffizient c: '))
print()

if a != 0.0:
    delta = b*b - 4.0*a*c
    if delta > 0.0:
        x1 = (-b + sqrt(delta))/(2.0*a)
        x2 = (-b - sqrt(delta))/(2.0*a)
        print("Die Gleichung hat zwei verschiedene reelle Lösungen:")
        print("x1 =", x1, "     ", "x2 =", x2)
    elif delta == 0.0:
        print("Die Gleichung hat eine reelle Lösung:")
        x1 = -b/(2.0*a)
        print("x1 = x2 =", x1)
    else:
        print("Die Gleichung hat keine reelle Lösungen.")
else:
    if b != 0.0:
        x = -c/b
        print("Die Gleichung ist linear und hat somit eine Lösung:")
        print("x =", x)
    else:
        if c != 0.0:
            print("Die Gleichung ist unlösbar!")
        else:
            print("Die Gleichung hat unendlich viele Lösungen!")