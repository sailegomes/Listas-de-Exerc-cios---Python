def calculadora_salario():
  salario_por_hora = input('Quanto você ganha por hora? ')
  horas_trab_mês = input('Quantas horas você trabalha no mês? ')
  salario_por_hora = float(salario_por_hora)
  horas_trab_mês = int(horas_trab_mês)
  salario_bruto = salario_por_hora * horas_trab_mês
  print(f'Salário Bruto: R${salario_bruto} ')
  imposto_renda = 0.11 * salario_bruto 
  print(f'IR: R${imposto_renda} ')
  valor_inss = 0.08 * salario_bruto
  print(f'INSS: R${valor_inss} ')
  valor_sindicato = 0.05 * salario_bruto
  print(f'Sindicato: R${valor_sindicato} ')
  salario_liquido = salario_bruto - imposto_renda - valor_inss - valor_sindicato
  print(f'Salário Líquido: R${salario_liquido}')  

calculadora_salario()
