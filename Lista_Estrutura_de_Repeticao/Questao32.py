#Questao 32

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída 
# deve ser conforme o exemplo abaixo:

# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

print(Fore.BLUE + '🔥🔥🔥  Bem-vindo(a) ao Factorial App  🔥🔥🔥' + Fore.RESET)
time.sleep(0.40)
numero = int(input('Insira o número que você deseja saber o fatorial: '))
print(f'Fatorial de: {numero}')
lista = []
for a in range(1,numero+1):
    lista.append(a)
print(f'{numero}! = ', end='')
for i in sorted(lista, reverse=True):
    print(i, end ='')
    print(' . ' if i > min(lista) else '', end = '' )
produto = 1
for valor in lista:
    produto *= valor
print(f' = {produto}')
