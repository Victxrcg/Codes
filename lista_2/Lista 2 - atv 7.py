class sort
def selection_sort(lista):
    n = len(lista)
    

    for i in range(n):
    
        menor_idx = i
    
        for j in range(i + 1, n):
            if lista[j] < lista[menor_idx]:
                menor_idx = j
        
        if menor_idx != i:
            lista[i], lista[menor_idx] = lista[menor_idx], lista[i]
    
    return lista
    
lista=[32,45,6,788,65,646]
sorted_lista = selection_sort(lista)
print(sorted_lista)