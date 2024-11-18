def multiplica_escalar(lista,escalar):
    return [elemento * escalar for elemento in lista]
numero=[1,2,3,4,5]
escalar = 3
resultado = multiplica_escalar (numero, escalar)
print(resultado)