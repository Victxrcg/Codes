def media_ponderada(lista_valores, lista_pesos):
    if len(lista_valores) != len(lista_pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")
    
    soma_pesos = sum(lista_pesos)
    soma_produtos = sum(v * p for v, p in zip(lista_valores, lista_pesos))
    
    return soma_produtos / soma_pesos if soma_pesos != 0 else 0

valores = [10, 20, 30]
pesos = [1, 2, 3]
print(media_ponderada(valores, pesos)) 
