#Questao 21

# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é 
# divisível somente por ele mesmo e por 1.

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
    lista = []
    for i in range(2,10):
        resto = numero%i
        lista.append(resto)
    produto = 1
    for valores in lista:
        produto *= valores
    if produto == 0:
        print(f'O número {numero} não é primo! ')   
    else:
        print(f'O número {numero} é primo! ')
