class conta():
    def __init__(self,number, holder, balance):
        self.number = number
        self.holder = holder
        self.balance = balance
    def deposit(self):
        self.depositar = float(input('valor deposito:'))
        self.balance = self.depositar + self.balance
        print(self.balance)

    def withdraw(self):
        self.saque = float(input('saque:'))
        self.balance = self.balance - self.saque
        print(self.balance)

conta1 = conta(1, 'Victor' ,0)
conta1.deposit()
conta1.withdraw()