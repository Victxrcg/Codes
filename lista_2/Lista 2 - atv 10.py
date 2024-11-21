def diferenca_max_min(lista):
    # Verifica se a lista não está vazia
    if not lista:
        return 0  # Ou pode lançar uma exceção, dependendo do comportamento esperado
    
    # Retorna a diferença entre o maior e o menor valor da lista
    return max(lista) - min(lista)
lista = [10, 20, 5, 7, 30]
resultado = diferenca_max_min(lista)
print(resultado)  # Saída: 25 (30 - 5)
