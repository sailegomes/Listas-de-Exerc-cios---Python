#Questao 16

# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até 
# que o valor seja maior que 500.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

print(Fore.BLUE + 'Seja muito bem-vindo(a) ao FIBONACCI APP. Sera gerado os numeros da sequencia ate que o valor seja maior '
      'do que 500 🔥🔥😁' + Fore.RESET)
time.sleep(0.23)
primeiro = 1
ultimo = 0
lista = []
for i in range(1, 100):
    while primeiro < 700:
        lista.append(primeiro)
        a = primeiro
        primeiro += ultimo
        ultimo = a
for valor in lista:
    print(valor, end = '')
    print(', ' if valor != max(sorted(lista)) else '.', end = '' )
    time.sleep(0.56)


