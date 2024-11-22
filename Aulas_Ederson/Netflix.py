class Usuario:
    def __init__(self, nome, email, cpf, plano, cartãodecredito, fone):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.plano = plano
        self.cartaodecredito = cartãodecredito 
        self.fone = fone
    
    def obternome(self):
        self.nome = input('digite seu nome:')
    def obteremail()