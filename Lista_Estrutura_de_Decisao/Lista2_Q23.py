def inteiro_ou_decimal():
    numero = float(input('\n Insira um número: '))
    if round(numero) == numero:
        print('\n O número inserido é inteiro.')
    else:
        print('\n O número inserido é decimal.')

inteiro_ou_decimal()
