senha=1234
decisao=0
extrato=0.0
saque=0.0
deposito=0.0
senha1=int(input("Digite a senha:"))
while decisao != '4':
    if senha1==senha :
        decisao=input("1-Extrato\n2-Deposito\n3-Saque\n4-Administrar\n")
        if decisao=='1' :
            print("Extrato da conta:",extrato)
        elif decisao== '2' :
            print("Digite o valor para deposito:")
            deposito=float(input())
            extrato= deposito + extrato
            print("\nExtrato é de:",extrato)
        elif decisao=='3':
            print("Informe um valor para saque:")
            saque=float(input())
            extrato= extrato-saque
            print("\nValor sacado foi de:",saque)
        elif decisao== '4':
            print("1-Cadastro\n2-Editar cadastro")
            decisao=int(input())
            if decisao == '1':
                nome=input("Digite seu nome:")
                cpf=input("Digite seu cpf:")
                fone=int(input("Digite seu telefone:"))
                sexo=input("Digite seu sexo:")
            elif decisao =='2':
                print("------DADOS-ATUAIS--------")
                print("Nome cadastrado:",nome)
                print("cpf cadastrado:",cpf)
                print("telefone cadastrado:",fone)
                print("sexo cadastrado:",sexo)
                print("--------------------------")
                nome=input("Digite seu nome:")

                

    else: 
        print("Senha invalida!")