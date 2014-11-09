#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

class Fahrrad:
    
    def __init__(self, marke, anz_zahnkraenze, anz_ritzel, zahnkranz, ritzel):
        self.__marke = marke
        self.__anz_zahnkraenze = anz_zahnkraenze
        self.__anz_ritzel = anz_ritzel
        self._zahnkranz = zahnkranz
        self._ritzel = ritzel
    
    def get_marke(self):
        return self.__marke
    
    def get_anz_zahnkraenze(self):
        return self.__anz_zahnkraenze
    
    def get_anz_ritzel(self):
        return self.__anz_ritzel
    
    def get_zahnkranz(self):
        return self._zahnkranz
    
    def get_ritzel(self):
        return self._ritzel
    
    def up_zahnkranz(self):
        if (self.get_zahnkranz() < self.get_anz_zahnkraenze()):
            self._zahnkranz += 1 # x += 1 ist äquivalent zu x = x + 1
    
    def down_zahnkranz(self):
        if (self.get_zahnkranz() > 1):
            self._zahnkranz -= 1
    
    def up_ritzel(self):
        if (self.get_ritzel() < self.get_anz_ritzel()):
            self._ritzel += 1
    
    def down_ritzel(self):
        if (self.get_ritzel() > 1):
            self._ritzel -= 1
            
    def print_zustand(self):
        print(self.get_marke(), end = " ")
        for i in range(self.get_anz_zahnkraenze()):
            if i == self.get_zahnkranz() - 1:
                print("*", end = "")
            else:
                print("o", end = "")
        print("----", end = "")
        for i in range(self.get_anz_ritzel()):
            if i == self.get_ritzel() - 1:
                print("*", end = "")
            else: print("o", end = "")    
        print()


def main():
    f = Fahrrad("Mountain Bike", 3, 10, 2, 5)
    f.print_zustand()
    f.up_ritzel()
    f.print_zustand()
    f.up_zahnkranz()
    f.up_zahnkranz()
    f.print_zustand()
    f.down_zahnkranz()
    f.up_ritzel()
    f.up_ritzel()
    f.up_ritzel()
    f.up_ritzel()
    f.print_zustand()
    f.down_zahnkranz()
    f.down_ritzel()
    f.down_ritzel()
    f.down_ritzel()
    f.print_zustand()
    f.down_zahnkranz()
    f.print_zustand()
    f.down_zahnkranz()
    f.print_zustand()
    g = Fahrrad("Mein Velo", 2, 5, 1, 1)
    g.print_zustand()
    print(g.get_marke(), "hat", g.get_anz_ritzel(), "Ritzel und", g.get_anz_zahnkraenze(), "Zahnkränze")

main()