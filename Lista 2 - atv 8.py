def insertion_sort(lista):
    # Começa a partir do segundo elemento (índice 1)
    for i in range(1, len(lista)):
        chave = lista[i]  # Elemento atual que precisa ser inserido na parte ordenada
        j = i - 1  # Índice do último elemento da parte ordenada
        
        # Move os elementos da parte ordenada para a direita, para abrir espaço
        # para o elemento chave
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Coloca a chave na posição correta
        lista[j + 1] = chave
        
    return lista
lista = [64, 25, 12, 22, 11]
sorted_lista = insertion_sort(lista)
print(sorted_lista)  # Saída: [11, 12, 22, 25, 64]
