def notas(nota1 , nota2):
    media = (nota1 + nota2)/2
    media = float(media)
    print(f'\n A média é igual a: {media}')
    if 0 <= media < 4:
        print('\n O aluno obteve conceito E. REPROVADO!')
    elif 4 <= media < 6:
        print('\n O aluno obteve conceito D. REPROVADO!')
    elif 6 <= media < 7.5:
        print('\n O aluno obteve conceito C. REPROVADO!')
    elif 7.5 <= media < 9:
        print('\n O aluno obteve conceito B. APROVADO!')
    else:
        print('\n O aluno obteve conceito A. APROVADO POR MÉDIA!!')

notas(10,9)
