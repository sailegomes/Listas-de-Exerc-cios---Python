def conversor_temperatura2():
  a = input('Insira um valor para a temperatura em graus Celcius: ')
  a = float(a)
  temperatura = round((a*(9/5))+32,2)
  print(f'A temperatura em graus Fahrenheit é igual a {temperatura}°F.')

conversor_temperatura2()
