produto=(input("Digite o nome do produto:"))
valor=float(input("Digite o valor do produto:"))
valor_importacao= (valor * 0.40) + valor

print(f"O valor da compra com o reajuste da importação é de: {valor_importacao:.2f}")