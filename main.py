# TRATAMENTOS DE ERROS

while True:
    try:
        a=int(input('Digite uma palavra:'))
    except ValueError:
        print('digite apenas numeros!')
    except:
        print('Erro desconhecido.')
    finally:
        print('Final do algoritimo')
   