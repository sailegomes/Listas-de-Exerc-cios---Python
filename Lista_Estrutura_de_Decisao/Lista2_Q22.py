def par_ou_impar():
    numero = int(input('\n Insira um número inteiro qualquer: '))
    if numero%2 == 0:
        print(f'\n{numero} é um número par.')
    else:
        print(f'\n{numero} é um número ímpar.')

par_ou_impar()
