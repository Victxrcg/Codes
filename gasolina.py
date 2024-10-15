litros=float(input("Digite a quantidade de litros:"))
resposta=input("Qual o tipo de combustivel? A ou G ? ")

g=2.50
a=1.90

if resposta == 'g' :
    if litros <= 20:
        valor=litros*2.50
        desc=valor*0.03
        valortotal= valor - desc
        print("Vc irá pagar:",valortotal)
    else:
        valor=litros*2.50
        desc=valor*0.05
        valortotal= valor - desc
        print("Vc irá pagar:",valortotal)

elif resposta == 'a' :
    if litros <= 20:
        valor=litros*1.90
        desc=valor*0.04
        valortotal= valor - desc
        print("Vc irá pagar:",valortotal)
    else:
        valor=litros*2.50
        desc=valor*0.06
        valortotal= valor - desc
        print("Vc irá pagar:",valortotal)
     
