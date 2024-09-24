
Nome_product=input("Digite o nome do produto:")
Preco=float(input("Digite o preço dos produtos:"))
quant=int(input("digite a quantidade dos produtos:"))
desc=int(input("Digite a quantidade de desconto:"))

desc = desc/100;

preco_total = Preco * quant
preco_total = preco_total - (desc * preco_total)
print("o preco total é de :R$",preco_total,"reais")