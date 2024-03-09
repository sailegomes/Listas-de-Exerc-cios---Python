#Questao 12

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar 
# de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

def tabuada():
    print(Fore.YELLOW + 'BEM-VINDO(A) AO REI DA TABUADA! 👑' + Fore.RESET)
    time.sleep(0.010)
    numero = int(input('Qual numero voce desejar saber a tabuada?'))
    for i in range(1,11):
         print(f'{numero}x{i} = {numero * i}')

tabuada()
