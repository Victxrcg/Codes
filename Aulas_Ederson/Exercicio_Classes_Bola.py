class Bola:
    def __init__(self,cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def Mostracor(self):
        print (f'A cor é:{self.cor}')  
    def trocarcor(self,cor):
        self.cor = cor  
        print(f'a cor mudou e ficou:{self.cor}')    

cor1=Bola ('Vermelha',15,'Nederite')
cor1.trocarcor()
cor1.Mostracor('verde')
# cor1.Mostracor()