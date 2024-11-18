while True:
    while True:
        nome=(input("Digite seu nome:"))
        if len(nome) <= 3 :
            print("Invalido")
        else:
            break
    
    while True:  
        idade=int(input("Digite sua idade:"))
        if idade < 0 or idade > 150 :
            print("invalido")  
        else:
            break
    while True:
        salario=float(input("Digite seu salario:"))
        if salario < 0:
            print("Salario precisa ser maior que zero!")
        else:
            break
    while True:    
        sexo=input("Digite o seu sexo com 'm','f' ou 'o' ")
        lista = ['m','f','o']
        if sexo not in lista:
            print(f"{lista}")
        else:
            break
    break

