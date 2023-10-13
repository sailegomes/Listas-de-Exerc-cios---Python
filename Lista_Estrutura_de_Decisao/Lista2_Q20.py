def notas(nota1,nota2,nota3):
    media = round((nota1 + nota2 + nota3)/3,1)
    if media == 10:
        print(f'Aprovado com Distinção. Nota: {media}.')
    elif media < 7:
        print(f'Reprovado. Nota: {media}.')
    else:
        print(f'Aprovado. Nota: {media}.')
notas(10,10,10)
