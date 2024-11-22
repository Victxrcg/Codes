# class Vendedor():
#     def __init__(self,nome,vendas):
#         self.nome = nome
#         self.vendas = vendas
class ControleRemoto:
    def __init__(self,cor, largura,altura,peso,canal):
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.peso = peso
        self.canal = ['Sbt','Globo','Record','Network']
        self.contador = -1

    def MudarDeCanal(self,botao):
        
        if botao =='+':
            self.contador +=1
            print('Aumentar canal')
            print(self.canal[self.contador])
        elif botao =='-':
            self.contador -=1
            print('Diminuir canal')
            print(self.canal[self.contador])
        else: 
            print('Valor invalido')


        def DesligarTv(self,botao):
            if botao == '1':
                print('Ligando...')
            elif botao == '0':
                print('Desligando...')
            else:
                print('A tv só liga e desliga!')





controle1 = ControleRemoto('amarelo', 10, 20, 30,4)

controle1.MudarDeCanal('+')

            