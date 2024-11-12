def consoantes_conta(texto):
    consoantes= 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTUVWXYZ'
    contador = 0 
    for caractere in texto:
        if caractere in consoantes:
            contador += 1

    return contador

texto= 'Exemplo sla isso aqui, quero dormir'
resultado = consoantes_conta(texto)
print(resultado)