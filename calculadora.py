escolha= 'sim'
while escolha=='sim':
    print("================Calculadora================")
    print("=1-Multiplicação                          =")
    print("=2-Divisão                                =")
    print("=3-Soma                                   =")
    print("=4-Subtração                              =")
    print("=5-Sair                                   =")
    print("================Calculadora================")
    decisao=input()
    if decisao =='1':
        valor1=int(input("Digite um valor para multiplicar:"))
        valor2=int(input("Digite um valor para multiplicar:"))
        conta=valor1*valor2
        print("Resultado:",conta)
    elif decisao =='2':
        valor1=int(input("Digite um valor para multiplicar:"))
        valor2=int(input("Digite um valor para multiplicar:"))
        conta=valor1/valor2
        print("Resultado:",conta)
    elif decisao =='3':
        valor1=int(input("Digite um valor para multiplicar:"))
        valor2=int(input("Digite um valor para multiplicar:"))
        conta=valor1+valor2
        print("Resultado:",conta)
    elif decisao =='4':
        valor1=int(input("Digite um valor para multiplicar:"))
        valor2=int(input("Digite um valor para multiplicar:"))
        conta=valor1-valor2
        print("Resultado:",conta)
    else: 
        break
    
