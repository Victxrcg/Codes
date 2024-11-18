perguntas=(input("Telefonou para a vitima?\n\n"))
perguntas1=(input("Esteve no local do crime?\n-Sim\n-Não\n"))
perguntas2=(input("Mora perto da vitima?\n-Sim\n-Não\n"))
perguntas3=(input("Devia algum dinheiro para a vitima?\n-Sim\n-Não\n"))
perguntas4=(input("Já trabalhou com a vitima?\n-Sim\n-Não\n"))

classificacao=0

if perguntas == 's':
    classificacao = classificacao +1
if perguntas1 == 's':
    classificacao = classificacao +1
if perguntas2 == 's':
    classificacao = classificacao +1
if perguntas3 == 's':
    classificacao = classificacao +1
if perguntas4 == 's':
    classificacao = classificacao +1

if (classificacao==2):
    print("Suspeito")
elif (classificacao==3) and (classificacao==4):
    print("Cumplice")
elif (classificacao==5):
    print("Assassino")
else:
    print("Inocente")
