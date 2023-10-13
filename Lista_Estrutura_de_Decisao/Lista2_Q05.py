def notas(a,b):
    media = (a+b)/2
    media = float(media)
    if(  7 <= media < 10):
        print('O aluno está APROVADO! Meus parabéns!')
    elif(media < 7):
        print('O aluno está REPROVADO! Hoje a chinela vai cantar.')
    else:
        print('O aluno está APROVADO COM DISTINÇÃO! Meus parabéns e sucesso!')

notas(5,6)
