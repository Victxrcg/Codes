def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    while esquerda and direita:
        if esquerda[0] < direita[0]:
            resultado.append(esquerda.pop(0))
        else:
            resultado.append(direita.pop(0))
    
    resultado.extend(esquerda)
    resultado.extend(direita)
    
    return resultado

lista = [3, 1, 4, 5, 2]
print(merge_sort(lista))  