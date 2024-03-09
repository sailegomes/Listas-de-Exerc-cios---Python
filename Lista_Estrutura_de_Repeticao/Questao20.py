#Questao 20

# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o 
# fatorial a números inteiros positivos e menores que 16.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

def fatorial():
    print(Fore.BLUE + '\n Ola, caro usuario! Insira um numero para comecarmos, por favor. 😁' + Fore.RESET)
    time.sleep(0.46)
    inteiro = int(input('Insira um numero inteiro: '))
    while inteiro < 0 or inteiro > 16:
        print('Insira um numero inteiro positivo e menor do que 16, por favor. ')
        inteiro = int(input('Insira um numero inteiro: '))
    time.sleep(0.46)
    print('O fatorial do numero inserido e: ')
    time.sleep(0.46)
    lista = []
    for i in range(1,inteiro+1):
        lista.append(i)
    print(f'{inteiro}!= ', end = '')
    for numero in sorted(lista, reverse=True):
        print(numero, end = '')
        print('.' if numero > 1 else '', end = '')
    produto = 1
    for number in lista: 
        produto *= number
    print(f'= {produto}', end = '')

fatorial()
pergunta = input('Gostaria de calcular algumm outro fatorial?(y/n) ')
while pergunta == 'y':
    fatorial()
 
