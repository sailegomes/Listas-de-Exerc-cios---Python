#Questao 8

# Faça um programa que leia 5 números e informe a soma e a média dos números.
import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time


def soma_media():
    lista = []
    while len(lista) < 5:
        valor = float(input('Insira um numero: '))
        lista.append(valor)
    print('Os numeros fornecidos foram: ')
    for i in lista:
        print(i, end = '')
        print(', ' if i != lista[4] else '.', end = '')
    print(Fore.BLUE + f'\n A soma dos numeros e: {sum(lista)}. ' + Fore.RESET)
    print(Fore.BLUE + f' A media dos numeros e: {np.mean(lista)}. ' + Fore.RESET)
    time.sleep(1)
    print('😁')


soma_media()
