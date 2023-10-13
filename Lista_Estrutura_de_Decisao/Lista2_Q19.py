def number_reader(numero):
    unidade = numero % 10
    numero1 = (numero - unidade)/10
    dezena = numero1 % 10
    centena = (numero1 - dezena)/10
    if numero <= 1:
        print(f'{numero} = {unidade} unidade.')
    elif (numero > 1) and (numero <= 9):
        print(f'{numero} = {unidade} unidades.')
    elif (numero > 9) and (numero <= 99):
        print(f'{numero} = {dezena} dezenas e {unidade} unidades.')
    else:
        print(f'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades.')

number_reader(618)
