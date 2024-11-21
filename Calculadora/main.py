import inquirer
from calculadora import Calculadora

def escolher_operacao():
    opcoes = [
        'Soma',
        'Subtração',
        'Multiplicação',
        'Divisão',
        'Sair'
    ]
    
    pergunta_opcao = [
        inquirer.List('operacao',
                      message="Escolha a operação",
                      choices=opcoes,
                      carousel=True),
    ]
    
    escolha = inquirer.prompt(pergunta_opcao)
    return escolha['operacao']

def obter_numeros():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    return numero1, numero2

def main():
    calculadora = Calculadora()

    while True:
        operacao = escolher_operacao()

        if operacao == 'Sair':
            print("Saindo da calculadora...")
            break

        numero1, numero2 = obter_numeros()
        resultado = calculadora.realizar_operacao(operacao, numero1, numero2)

        print(f"O resultado da operação {operacao} é: {resultado}")
        
        continuar = inquirer.prompt([
            inquirer.Confirm('continuar',
                             message="Deseja realizar outra operação?",
                             default=True),
        ])
        
        if not continuar['continuar']:
            print("Saindo da calculadora...")
            break

if __name__ == '__main__':
    main()
