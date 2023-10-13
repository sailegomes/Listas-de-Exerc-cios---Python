def operacoes():
  a = input('Insira um número inteiro: ')
  b = input('Insira outro número inteiro: ')
  c = input('Agora, insira qualquer número real: ')
  a,b,c=int(a),int(b),float(c)
  primeira_operacao = (a*2) * (b/2)
  segunda_operacao = (a*3) + c
  terceira_operacao = c**3
  print(f'Resposta do item a): {primeira_operacao}')
  print(f'Resposta do item b): {segunda_operacao}')
  print(f'Resposta do item c): {terceira_operacao}')
  

operacoes()
