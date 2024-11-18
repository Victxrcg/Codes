nome=str(input("Digite seu nome:"))
idade=int(input("Digite sua idade:"))
sexo=str(input("Digite seu sexo:"))
nota1=int(input("Digite sua nota1:"))
nota2=int(input("Digite sua nota2:"))

notas= (nota1 + nota2) / 2

print(f"Aluno:",nome,"\nidade:",idade,"\nsexo:",sexo,"\nA sua media é de:",notas)