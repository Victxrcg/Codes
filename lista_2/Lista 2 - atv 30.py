def histograma(lista):
    ocorrencias = {}
    for item in lista:
        ocorrencias[item] = ocorrencias.get(item, 0) + 1
    return ocorrencias

# Exemplo de uso
lista = [1, 2, 2, 3, 3, 3]
print(histograma(lista))  # Saída esperada: {1: 1, 2: 2, 3: 3}
