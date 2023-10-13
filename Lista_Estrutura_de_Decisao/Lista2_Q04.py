def letras():
    a = input('Digite uma letra qualquer: ')
    b = ['a','e','i','o','u']
    if(a in b):
        print('A letra inserida é uma vogal.')
    else:
        print('A letra inserida é uma consoante.')

letras()
