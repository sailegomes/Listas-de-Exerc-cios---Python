def investigacao():
    lista = []
    print('\n Olá! Por favor, responda às perguntas, com "sim" ou "não", da forma mais sincera possível. Lembre-se, '
          'você está sob juramento e se mentir será preso(a)!')
    pergunta1 = input('\n Você telefonou para a vítima? ')
    lista.append(pergunta1)
    pergunta2 = input('\n Você Esteve no local do crime? ')
    lista.append(pergunta2)
    pergunta3 = input('\n Você mora perto da vítima? ')
    lista.append(pergunta3)
    pergunta4 = input('\n Você possuía pendências financeiras com a vítima? ')
    lista.append(pergunta4)
    pergunta5 = input('\n Você já trabalhou com a vítima? ')
    lista.append(pergunta5)
    contador = lista.count('sim')
    if contador == 2:
        print('\n Atenção, oficial. Considere o indivíduo como SUSPEITO!')
    elif (contador == 3) or (contador == 4):
        print('\n Atenção, oficial. Considere o indivíduo como CÚMPLICE!!')
    elif contador == 5:
        print('\n Atenção, oficial. PRENDA ESTE INDIVÍDUO IMEDIATAMENTE, ELE É O ASSASSINO!!!!!')
    else:
        print('\n Atenção, oficial. Por favor, libere este indivíduo porque ele é INOCENTE.')

investigacao()
