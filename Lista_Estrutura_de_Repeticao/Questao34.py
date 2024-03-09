#Questao 34

# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo 
# é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine
# se ele é ou não um número primo.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

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
