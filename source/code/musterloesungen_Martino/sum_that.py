#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

summe = 0
for i in range(10000):
    if (i % 7 == 0) and (i % 5 != 0):
        summe = summe + i
    
print("Die Summe aller natürliche Zahlen < 10'000, die durch 7 aber nicht durch 5 teilbar sind, ist :", summe) 