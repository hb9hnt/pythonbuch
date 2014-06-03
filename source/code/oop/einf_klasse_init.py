# Neuer Bauplan für eine Person:
# Beim Erstellen eines Objekt der Klasse Person
# werden die Instanzvariablen direkt definiert.
class Person:
    def __init__(self, name, vorname, geb_datum, gewicht):
        self.name = name
        self.vorname = vorname
        self.geb_datum = geb_datum
        self.gewicht = gewicht

    def vorstellen(self):
        text = "Hallo.\nIch heisse " \
               + self.vorname + " " \
               + self.name + ", wiege " \
               + self.gewicht + " und habe am " \
               + self.geb_datum + " Geburtstag.\n"\
               + "Nice to meet you."
        print(text)

    def abnehmen(self, wie_viel):
        print("Altes Gewicht:",self.gewicht)
        
        # Das aktuelle Gewicht in einen Float umwandeln
        # um subtrahieren zu können
        pos = self.gewicht.find(" ")
        neues_gew = float(self.gewicht[0:pos]) - wie_viel

        # Das neue Gewicht wieder in einen String konvertieren
        # und in die Instanzvariable speichern
        self.gewicht = str(neues_gew) + " kg"
        print("Neues Gewicht:",self.gewicht)

        return ("Neues Gewicht: " + self.gewicht)
