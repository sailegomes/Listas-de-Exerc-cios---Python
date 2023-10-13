def mensagem():
    a = input('\n Em qual turno você estuda? \n Por favor, digite M-matutino, V-vespertino ou N-noturno.')
    if a == 'M':
        print('\n Bom dia!')
    elif a == 'V':
        print('\n Boa tarde!')
    elif a == 'N':
        print('\n Boa noite!')
    else:
        print('\n Valor inválido, jerk!')


mensagem()
