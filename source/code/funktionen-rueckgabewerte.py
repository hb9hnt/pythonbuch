def add_multiply(zahl1, zahl2):
    return zahl1+zahl2, zahl1*zahl2

a = add_multiply(4,10)
print(a, a[0], a[1])

a, b = add_multiply(4,10)
print(a, b)
