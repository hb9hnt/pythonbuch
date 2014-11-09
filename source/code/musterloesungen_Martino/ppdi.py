#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

print()
print("*-----------------------------------*")
print("* Liste aller PPDI mit drei Ziffern *")
print("*-----------------------------------*")
print()

for i in range(100, 1000):
    hunderterstelle = i // 100
    zehnerstelle = (i - 100*hunderterstelle) // 10
    einheiten = i % 10
    s = hunderterstelle**3 + zehnerstelle**3 + einheiten**3
    if (i == s):
        print(i)