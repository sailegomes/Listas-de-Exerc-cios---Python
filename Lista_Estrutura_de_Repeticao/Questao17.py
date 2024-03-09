#Questao 17

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

print(Fore.BLUE + 'Ola, caro usuario! Insira um numero para comecarmos, por favor. 😁' + Fore.RESET)
time.sleep(0.56)
inteiro = int(input('Insira um numero inteiro: '))
time.sleep(0.56)
print('O fatorial do numero inserido e: ')
time.sleep(0.56)
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



