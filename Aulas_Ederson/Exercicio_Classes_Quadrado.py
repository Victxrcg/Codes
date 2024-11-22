class Quadrado:
    def __init__(self,lado):
        self.lado = lado
    
    def calcular(self):
        return self.lado ** 4
    def area(self):
        return self.lado ** 2

lado1 = Quadrado(2)
print (lado1.calcular())
print (lado1.area())

        