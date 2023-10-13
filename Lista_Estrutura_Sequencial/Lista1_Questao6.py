def area_circulo():
  import math
  r = input('Raio do círculo (cm): ')
  r = float(r)
  area = round(math.pi*(r**2),2)
  print(f'A área do círculo é {area} cm².')

area_circulo()
