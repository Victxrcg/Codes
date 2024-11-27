class conta():
    def __init__(self,number: int, holder: str, balance: float):
        self.number = number
        self.holder = holder
        self.balance = balance
    def deposit(self):
        self.depositar = float(input('valor deposito:'))
        self.balance = self.depositar + self.balance
        print(self.balance)

    def withdraw(self):
        saque = float(input('saque:'))
        if saque <= self.balance:
            saque = self.balance - self.saque
            print(self.balance)

class contaempresarial (conta):
    def __init__(self, number: int, holder: str , balance: float, loanlimit : float):
        super().__init__(number, holder, balance)
        self.loanlimit = loanlimit
        
    def loan(self,amount : float):
        if amount <= self.loanlimit:
            self.balance = self.balance + amount
            self.loanlimit = self.loanlimit - amount
            print(f'Foi adicionado o valor de {amount} na conta.\nVoce agora possui {self.balance} em sua conta.\nVoce tem apenas {self.loanlimit} para emprestimo.')
        else:
            print('Voce nao pode sacar tudo')

conta1 = contaempresarial(2,'contadovictor',0,2000)
conta1.loan(2000)
conta1.deposit()
conta1.withdraw()