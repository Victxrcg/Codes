while True:
    nome=(input("Digite seu nome:"))
    senha=(input("Digite sua senha:"))
    if senha == nome:
        print("Senha nao pode ser igual usuario")
    else:
        print("Bem vindo")
        break