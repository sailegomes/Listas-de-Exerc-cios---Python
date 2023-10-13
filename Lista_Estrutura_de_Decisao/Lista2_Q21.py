def dinheiro():
    valor0 = int(input('Qual o valor de saque? '))
    cem = int(valor0/100)
    valor1 = valor0 - cem*100
    cinquenta = int(valor1/50)
    valor2 = valor1 - cinquenta*50
    dez = int(valor2/10)
    valor3 = valor2 - dez*10
    cinco = int(valor3/5)
    valor4 = valor3 - cinco*5
    um = int(valor4/1)
    if valor0 < 10:
        print('\n O valor mínimo para saque é de R$20,00. Por favor, selecione um valor válido. ')
    elif valor0 > 600:
        print('\n O valor máximo para saque é de R$600,00. Por favor, selecione um valor válido.')
    else:
        print(f'\n Notas de R$100,00: {cem}')
        print(f'\n Notas de R$50,00: {cinquenta}')
        print(f'\n Notas de R$10,00: {dez}')
        print(f'\n Notas de R$5,00: {cinco}')
        print(f'\n Notas de R$1,00: {um}')

dinheiro()
