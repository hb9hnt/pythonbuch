#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

# Wir brauchen die Zahl pi von der Library "math"
from math import pi

rad = float(input("Winkel in Bogenmass eingeben: "))
deg = rad*180.0/pi
grad = int(deg)
bogenmin = int((deg - grad)*60)
bogenmin = ((deg - grad)*60 - bogenmin)*60
print(rad, " rad = ", grad, "°", bogenmin, "'", bogenmin, "\"", sep = "")
