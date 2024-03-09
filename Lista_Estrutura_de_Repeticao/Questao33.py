#Questao 33

# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado 
# de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

print(Fore.BLUE + '🔥🔥🔥  Bem-vindo(a) ao Temparatura App  🔥🔥🔥' + Fore.RESET)
temperaturas = []
temperatura = 1
time.sleep(0.30)
print('Olá! Digite à vontade as temperaturas que desejar, e ao final digite 0 para obter os resultados.')
while temperatura != 0:
    temperatura = float(input('Insira as temperaturas: '))
    temperaturas.append(temperatura)
temperaturas.remove(0)
time.sleep(0.30)
print('##### RESULTADOS #####')
print(f'Menor temperatura: {min(temperaturas)}')
print(f'Maior temperatura: {max(temperaturas)}')
print(f'Médias das temperaturas: {np.mean(temperaturas)}')
