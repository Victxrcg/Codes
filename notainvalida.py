while True: 
    valor=float(input("Digite um valor:"))
    if valor >= 0 and valor <= 10:
        print("Nota valida")
        break
    else:
        print("invalido")