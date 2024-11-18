def diferenca_elementos_lista(lista):
    if len(lista) < 2:
        return []  
    diferencas = []
    for i in range(1, len(lista)):
        diferenca = abs(lista[i] - lista[i-1])
        diferencas.append(diferenca)
    
    return diferencas

lista = [10,5]
print(diferenca_elementos_lista(lista))  
