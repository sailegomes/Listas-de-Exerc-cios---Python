#"Com parâmetro":
def conversor(a):
  b = a*100
  print(f'{b} cm.')

#"Sem parâmetro":
def converso_r():
  valor = input('Digite o valor a ser convertido: ')
  valor = float(valor)
  valor = valor*100
  print(f'{valor} cm')

conversor(20.5)
