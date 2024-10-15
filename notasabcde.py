nota1=float(input("Digite sua nota:"))
nota2=float(input("Digite sua nota:"))
media= (nota1 + nota2) / 2 
if media >= 9 and media == 10:
    nota= 'A'
    situacao= 'Aprovado'
elif media >= 7.6 and media <=9:
    nota='B'
    situacao= 'Aprovado'
elif media >= 6 and media<= 7.5:
    nota='C'
    situacao='Aprovado'
elif media >= 4.1 and media<= 5.9:
    nota='D'
    situacao='Reprovado'
elif media <= 4.0:
    nota='E'
    situacao='Reprovado'   
    
print("A primeira nota é:",nota1)
print("A primeira nota é:",nota2)
print("A media é:",media)
print("A nota é de:",nota)
print("A situação é:",situacao)
   

    
    