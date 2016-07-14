class Fahrzeug:
    def __init__(self, marke, hubraum, leistung):
        self.marke = marke
        self.hubraum = hubraum
        self.leistung = leistung

    def get_infos(self):
        return "Marke: " + self.marke + ", Hubraum: " + \
    str(self.hubraum) + ", Leistung: " + str(self.leistung)

class Personenwagen(Fahrzeug):
    def __init__(self, marke, hubraum, leistung, anz_plaetze):
        super().__init__(marke, hubraum, leistung)
        self.anz_plaetze = anz_plaetze
    
    def get_infos(self):
        return super().get_infos() + ", Anzahl Plaetze: " + str(self.anz_plaetze)
    
class Lastwagen(Fahrzeug):
    def __init__(self, marke, hubraum, leistung, last):
        super().__init__(marke, hubraum, leistung)
        self.last = last

    def get_infos(self):
        return super().get_infos() + ", Lastgewicht: " + str(self.last)

if __name__ == "__main__":
    pw = Personenwagen("Opel", 222, 100, 5)
    lkw = Lastwagen("Mercedes", 5000, 300, 2000)
    print(pw.get_infos())
    print(lkw.get_infos())
