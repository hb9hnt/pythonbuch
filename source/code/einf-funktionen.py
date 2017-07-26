from random import randint

eingabe = int(input("Gib eine positive ganze Zahl an: "))

liste = []
for i in range(eingabe):
    liste.append(randint(0,100))

result = 0
for i in range(eingabe):
    result = result + liste[i]
    
result = result / len(liste)

print("Das Ergebnis lautet " + str(result) + ".")
