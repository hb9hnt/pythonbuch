class Fahrrad:
    
    '''
    Hier definierst du die Methoden (__init__() Methode nicht vergessen)
    '''


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