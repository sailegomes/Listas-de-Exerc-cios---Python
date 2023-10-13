def conversor_temperatura():
  a = input('Insira um valor para a temperatura em graus Fahrenheit: ')
  a = float(a)
  temperatura = round(5 * ((a-32)/9),2)
  print(f'A temperatura em graus Celsius é igual a {temperatura}°C.')

conversor_temperatura()
