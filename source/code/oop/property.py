class Motorrad():
    def __init__(self, marke, hubraum):
        self.marke = marke
        self.__hubraum = hubraum

    def set_hubraum(self, kubik):
        if (kubik <= 0):
            print("Error: Negativer Wert für den Hubraum! \
Der Wert wurde nicht geändert")
        else:
            self.__hubraum = kubik
            print("Hubraum wurde geändert.")

    def get_hubraum(self):
        return self.__hubraum

    hubraum = property(get_hubraum, set_hubraum)

if __name__ == "__main__":
    motrad = Motorrad("Suzuki", 250)
    print(motrad.hubraum)
    motrad.hubraum = -40
    print(motrad.hubraum)
    motrad.hubraum += 50
    print(motrad.hubraum)
