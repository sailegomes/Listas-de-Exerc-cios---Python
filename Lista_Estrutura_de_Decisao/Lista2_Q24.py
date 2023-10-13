def operacao(primeiro,segundo):
    resposta = input('\n Qual operação você deseja realizar? ')
    soma = primeiro+segundo
    subtracao = primeiro-segundo
    produto = primeiro*segundo
    divisao = primeiro/segundo
    if resposta == 'soma':
        print(f'\n O resultado é {soma}.')
    elif resposta == 'subtracao':
        print(f'\n O resultado é {subtracao}.')
    elif resposta == 'produto':
        print(f'\n O resultado é {produto}.')
    else:
        print(f'\n O resultado é {divisao}.')

operacao(5,10)
