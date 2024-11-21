def diferenca_conjunto(list1,list2):
    return (list(set(list1)- set (list2)))
list1 = [1,2,3,4,5]
list2 = [2,4,6,7,8]
reslutado = diferenca_conjunto(list1 , list2)
print ( reslutado )

# A função set(lista1) converte a lista1 em um conjunto, eliminando elementos duplicados e 
# permitindo operações eficientes de diferença.
# A operação set(lista1) - set(lista2) retorna um novo conjunto contendo os 
# elementos que estão em lista1 e não em lista2. 