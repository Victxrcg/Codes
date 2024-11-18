idade=int ( input("Digite sua idade:"))
if idade == 16: 
    print("Pode votar")
else:
    if idade >= 18:
        print("Pode dirigir")
    else:
        if idade <16 :
            print ("Apenas estude")
