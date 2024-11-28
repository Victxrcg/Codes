# import matplotlib.pyplot as plt
# x= [1,2,3,4,5]
# y= [2,4,9,16,25]
# plt.plot(x,y,label='Crescimento')
# plt.title('Grafico simples')
# plt.xlabel('Eixo X')
# plt.xlabel('Eixo Y')
# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
import random

lista_cara = []
cara = 0
lista_coroa = []
jogada = []
coroa = 0
jogadas = 50

for i in range(1, jogadas + 1):  
    escolha = random.randint(1, 2)  
    if escolha == 1:
        lista_coroa.append(coroa / i)
        cara += 1
        lista_cara.append(cara/i)
        jogada.append(i)
    else:
        lista_cara.append(cara/i)
        coroa += 1
        lista_coroa.append(coroa / i)
        jogada.append(i)

#lista_cara <-- lista para cara 
#lista_coroa <-- lista para coroa
#jogada <-- lista de jogadas