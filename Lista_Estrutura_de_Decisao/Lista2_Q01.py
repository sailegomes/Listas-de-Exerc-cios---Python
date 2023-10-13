def numeros():
    a = input('\nOlá, usuário! Insira um número: ')
    a = float(a)
    b = input('\nAgora, insira um segundo número: ')
    b = float(b)
    if(a > b):
        print(f'\n O maior número inserido foi o {a}!')
    else:
        print(f'\n O maior número inserido foi o {b}!')

numeros()
