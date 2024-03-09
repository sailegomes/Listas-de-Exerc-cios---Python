#Questao 7

# Faça um programa que leia 5 números e informe o maior número.
import pandas as pd
from colorama import Fore, Back, Style
import time


def leitor():
    lista = []
    while len(lista) < 5:
        obs = float(input('Insira um numero: '))
        lista.append(obs)
    print('A lista fornecida foi: ')
    for i in lista:
        print(i, end = '')
        print(', ' if i != lista[4] else '.', end = '')
    time.sleep(1.5)
    print(Fore.BLUE + f'\n O maior numero da lista fornecida e {max(lista)}. 🔥' + Fore.RESET)
    
        
leitor()
