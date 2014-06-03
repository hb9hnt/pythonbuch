def temp_funktion(x):
    return x + 42

def make_list(f,groesse):
    ergebnis = []
    for i in range(groesse):
        ergebnis.append(f(i))
    return ergebnis

a = make_list(temp_funktion, 5)
print(a)
