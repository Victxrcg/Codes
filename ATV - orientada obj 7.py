
def vogal(texto):
    c=0
    for i in range (0,len(texto)):
        if 'a' == texto[i] or 'e' == texto[i] or 'i' == texto[i] or 'o' == texto[i] or 'u' == texto[i]:
            c=c+1
    print(c)


vogal('abacate')
