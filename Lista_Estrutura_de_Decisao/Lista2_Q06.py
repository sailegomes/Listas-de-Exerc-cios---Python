def numeros(a,b,c):
    if(a>b) and (a>c):
        print(f'O maior número é o {a}.')
    elif(b>a) and (b>c):
        print(f'O maior número é o {b}.')
    else:
        print(f'O maior número é o {c}')

numeros(2,7,13)
