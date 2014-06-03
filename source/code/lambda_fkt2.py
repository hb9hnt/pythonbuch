def make_list(f,groesse):
    ergebnis = []
    for i in range(groesse):
        ergebnis.append(f(i))
    return ergebnis

a = make_list(lambda x: x + 42, 5)
print(a)
