def media_notas():
  primeira = input('Valor da primeira nota: ')
  primeira = int(primeira)
  segunda = input('Valor da segunda nota: ')
  segunda = int(segunda)
  terceira = input('Valor da terceira nota: ')
  terceira = int(terceira)
  quarta = input('Valor da quarta nota: ')
  quarta = int(quarta)
  soma = primeira+segunda+terceira+quarta
  media = soma/4
  if(media >= 7):
    print(f'A média das notas bimestrais é: {media}. Parabéns, você passou!')
  else:
    print(f'A média das notas bimestrais é: {media}. Lamento, mas você reprovou!')

media_notas()
