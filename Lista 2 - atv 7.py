def selection_sort(lista):
    n = len(lista)
    
    # Passa por cada elemento da lista
    for i in range(n):
        # Assume que o menor elemento está na posição i
        menor_idx = i
        
        # Encontra o menor elemento na sublista que começa na posição i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_idx]:
                menor_idx = j
        
        # Se o menor elemento não estiver na posição i, faz a troca
        if menor_idx != i:
            lista[i], lista[menor_idx] = lista[menor_idx], lista[i]
    
    return lista
lista=[32,45,6,788,65,646]
sorted_lista = selection_sort(lista)
print(sorted_lista)