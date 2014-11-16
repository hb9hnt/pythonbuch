#!/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Martino Antognini (uzh)

def encrypt(s, n):
    L = []
    for x in s:
        if x.isalpha():
            if 65 <= ord(x) <= 90:    # Grossbuchstabe
                L.append(chr(((ord(x) - 65 + n) % 26) + 65))
            if 97 <= ord(x) <= 122:   # Kleinbuchstabe
                L.append(chr(((ord(x) - 97 + n) % 26) + 97))
        else:
            L.append(x)  # x ist keine Buchstabe
    return "".join(L)


def decrypt(s, n):
    return encrypt(s, -n)
    
    
def main():
    print("Bitte Zeichenkette eingeben:")
    s = input()
    n = -1
    while n < 0 or n > 26:
        n = int(input("Bitte Schlüssel eingeben (natürliche Zahl zwischen 0 und 26): "))
    print()
    encrypted = encrypt(s, n)
    print("Verschlüsselte Nachricht:\n", encrypted)
    decrypted = decrypt(encrypted, n)
    print("Entschlüsselte Nachricht:\n", decrypted)
    
main()    
