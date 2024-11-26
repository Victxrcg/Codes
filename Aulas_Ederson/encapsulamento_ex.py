class Conta():
    def __init__(self,nome,saldo,cpf,senha):
        self.__nome = str
        self.__saldo = float
        self.__cpf = str
        self.__senha = int
    def depositar(self,saldo):
        depositar = float(input('Digite o valor que deseja depositar:'))
        self.extrato = self.saldo + depositar
        print ('Depositado.')
    def Extrato (self,senha):
        self.senhaver = int(input('Digite a senha:'))
        if self.senhaver == senha:
            return print(self.__saldo)
        else:
            print('Senha incorreta!')
    def sacar(self,senha):
        if self.senhaver == senha:
            self.saque = float(input('Digite o valor do saque:'))
            self.__saldo