#Questao 10

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

def intervalo():
    a = int(input('Insira um numero: '))
    b = int(input('Insira um segundo numero: '))
    print('Os numeros sao:')
    for i in range(a+1,b):
        print(i, end='')
        print(', ' if i != max(range(a+1,b)) else '.', end = '')

intervalo()
