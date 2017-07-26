from random import randint

def zufallsliste_erstellen(eine_zahl):
    liste = []
    for i in range(eine_zahl):
        liste.append(randint(0,100))
    return liste

def berechne_mittelwert(eine_liste):
    result = 0
    for i in range(len(eine_liste)):
        result = result + eine_liste[i]

    result = result / len(eine_liste)

    print("Das Ergebnis lautet " + str(result) + ".")

# Hauptprogramm
eingabe = int(input("Gib eine positive ganze Zahl an: "))
zufallsliste = zufallsliste_erstellen(eingabe)
berechne_mittelwert(zufallsliste)
