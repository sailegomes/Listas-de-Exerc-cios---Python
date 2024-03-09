#Questao 22

# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time

print(Fore.BLUE + 'Ola, usuario! Seja muito bem-vindo(a) ao Cousin App 🔥' + Fore.RESET)
numero = int(input('Por favor, digite um numero inteiro qualquer: '))
while numero == 1 or numero < 0:
    print('Digite outro numero, cegonha.')
    numero = int(input('Por favor, digite um numero inteiro qualquer: '))
if numero == 3 or numero == 5 or numero == 7:
    print(f'O numero {numero} é primo.')
else:
    lista_divisiveis = []
    lista = []
    for i in range(2,10):
        resto = numero%i
        lista.append(resto)
        if resto == 0:
            lista_divisiveis.append(i)
produto = 1
for valores in lista:
    produto *= valores
if produto == 0:
    print(f'O número {numero} não é primo! ')
    print(f'O número {numero} é divisível por: ', end = '')
    if len(lista_divisiveis) != 2:
        for divisores in lista_divisiveis:
            print(divisores, end='')
            print(', ' if divisores < max(sorted(lista_divisiveis)) else '.', end = '')
    else:
        for divisores in lista_divisiveis:
            print(divisores, end='')
            print(' e ' if divisores < max(sorted(lista_divisiveis)) else '.', end = '')
else:
    print(f'O número {numero} é primo! ')
