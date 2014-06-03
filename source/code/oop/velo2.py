class Velo():
    def __init__(self, farbe, alter=0):
        self.farbe = farbe
        self.alter = alter
        
v1 = Velo("gelb", 5)
v2 = Velo("rot")
print(v1.alter)
print(v2.alter)
