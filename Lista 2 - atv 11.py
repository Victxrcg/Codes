def escalar_vetores(vetor1, vetor2):
    soma = 0
    for i in range (0,len(vetor1)):
        soma +=  vetor1[i]*vetor2[i]
    return soma 

vetor1 = [ 1 , 2]
vetor2 = [ 2 , 4]
    
print(escalar_vetores(vetor1, vetor2))