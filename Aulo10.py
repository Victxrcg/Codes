while True:
    try:
        print('1-Multiplicação')
        print('2-Divisão')
        print('3-Subtração')
        print('4-Adição')
        print('5-Sair')
        escolha=int(input("digite oque deseja:"))
        if escolha == 1:
            a=float(input('digite um numero:'))
            b=float(input('digite um numero:'))
            conta=a*b
            print('A multiplicação é de:',conta)
        elif escolha == 2:
            a=float(input('digite um numero:'))
            b=float(input('digite um numero:'))
            conta=a/b
            print('A Divisão é de:',conta)
        elif escolha == 3:
            a=float(input('digite um numero:'))
            b=float(input('digite um numero:'))
            conta=a/b
            print('A Subtração é de:',conta)
        elif escolha == 4:
            a=float(input('digite um numero:'))
            b=float(input('digite um numero:'))
            conta=a/b
            print('A Adição é de:',conta)
        elif escolha == 5:
            print('Saindo...')
            break
        else:
            print('escolha invalida')
    except:
        print('Apenas numeros!')