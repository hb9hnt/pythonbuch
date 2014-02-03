antwort = input('Beantworte die Frage mit Ja oder Nein (J/N): ')

while antwort not in ['j', 'J', 'n', 'N']:
    print('Eingabe ungültig!')
    antwort = input('Beantworte die Frage mit Ja oder Nein (J/N): ')

print('Vielen Dank!')
