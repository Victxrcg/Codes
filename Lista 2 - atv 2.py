def produtos_lista(lista):
    resultado =1 
    for numero in lista:
        resultado *= numero
    return resultado
numeros = [2,3,4,5]
resultado = produtos_lista(numeros)
print (resultado)