#Questao 11

# Altere o programa anterior para mostrar no final a soma dos números.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

def intervalo2():
    a = int(input('Insira um numero: '))
    b = int(input('Insira um segundo numero: '))
    print('Os numeros sao:')
    lista = []
    for i in range(a+1,b):
        lista.append(i)
        print(i, end='')
        print(', ' if i != max(range(a+1,b)) else '.', end = '')
    print(Fore.BLUE + f'\n A soma dos numeros e: {sum(lista)}.' + Fore.RESET)

intervalo2()
