salario=float(input("Digite seu salario:"))
if salario <= 280:
    aumento=salario*0.20 + salario
    print("O seu salario com aumento de 20% vai para:",aumento)
elif salario > 280 and salario <700:
    aumento=salario*0.15 + salario
    print("O seu salario com aumento de 15% vai para:",aumento)
elif salario > 700 and salario <1500:
    aumento=salario*0.10 + salario
    print("O seu salario com aumento de 10% vai para:",aumento)
elif salario > 1500:
    aumento=salario*0.05 + salario
    print("O seu salario com aumento de 5% vai para:",aumento)
