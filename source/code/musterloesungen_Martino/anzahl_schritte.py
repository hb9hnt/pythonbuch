#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

a = int(input("Bitte natürliche Zahl a eingeben: "))
while a < 0:
    print("Falsche Eingabe!")
    a = int(input("Bitte natürliche Zahl a eingeben: "))
    
b = int(input("Bitte natürliche Zahl b grösser oder gleich a eingeben: "))
while b < a:
    print("Falsche Eingabe!")
    b = int(input("Bitte natürliche Zahl b grösser oder gleich a eingeben: "))   
    

for i in range(a, b + 1):
    n = i
    counter = 0
    while n != 0:
        counter = counter + 1
        if (n % 3) == 0:
            n = n + 4
        else:
            if (n % 4) == 0:
                n = n // 2
            else:
                n = n - 1
    print(i, "->", counter)    