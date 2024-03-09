#Questao 18

# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

def valores():
    quantidade = int(input('Quantos valores voce ira inserir? '))
    lista = []
    time.sleep(0.50)
    while len(lista) < quantidade:
        valores = float(input('Insira os valores: '))
        lista.append(valores)
    menor = min(lista)
    maior = max(lista)
    soma = sum(lista)
    print('######### Os resultados sao: #########')
    print(f'Maior valor: {maior}')
    print(f'Menor valor: {menor}')
    print(f'Soma: {soma}')


valores()
