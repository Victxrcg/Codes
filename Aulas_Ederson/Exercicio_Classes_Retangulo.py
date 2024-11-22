class Retangulo:
    def __init__(self,LadoA,ladoB):
        self.LadoA = LadoA
        self.LadoB = ladoB
    def pedir(self,ladoA,ladoB):
        self.LadoA = float(input('Digite o ladoA:'))
        self.LadoB = float(input('Digite o ladoB:'))
        return print(self.LadoA , self.LadoB)

    def calcular(self):
        return self.LadoA * self.LadoB
    def perimetro(self):
        return ((self.LadoA * 2) + (self.LadoB * 2))

Retangulo1 = Retangulo(0,0)
Retangulo1.pedir(0,0)
print(Retangulo1.calcular())
print(Retangulo1.perimetro())