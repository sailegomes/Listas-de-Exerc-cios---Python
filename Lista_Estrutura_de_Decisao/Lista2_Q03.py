def genero():
    a = input('Insira o seu sexo: ')
    if(a == 'M'):
        print('M - Masculino')
    elif(a == 'm'):
        print('M - Masculino')
    elif(a == 'F'):
        print('F - Feminino')
    elif(a == 'f'):
        print('F - Feminino')
    else:
        print('Sexo inserido inválido.')

genero()
