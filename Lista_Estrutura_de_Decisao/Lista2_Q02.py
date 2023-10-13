def polaridade():
    a = input('\n Insira um número qualquer: ')
    a = float(a)
    if(a>0):
        print('\n O número inserido é positivo.')
    elif(a<0):
        print('\n O número inserido é negativo.')
    else:
        print('\n O número inserido foi o zero.')

polaridade()
