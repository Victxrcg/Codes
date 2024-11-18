nota1=int(input("Digite sua nota:"))
nota2=int(input("Digite sua nota:"))
nota3=int(input("Digite sua nota:"))
nota4=int(input("Digite sua nota:"))
resultado = (nota1 + nota2 + nota3 + nota4) /4
if resultado == 10:
    print("Aprovado com distinção")
elif resultado <= 7:
    print("reprovado")
elif resultado >= 7:
    print("Aprovado")
