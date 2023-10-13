def curiar_o_seu_salario():
  a = input('Quanto você ganha por hora? ')
  a = float(a)
  b = input('Quantas horas você trabalhou no mês? ')
  b = int(b)
  salario = a*b
  print(f'O seu salário nesse mês é de R${salario}')

curiar_o_seu_salario()
