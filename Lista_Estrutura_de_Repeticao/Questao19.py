#Questao 19

# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

def valores():
    quantidade = int(input('Quantos valores voce ira inserir? '))
    lista = []
    time.sleep(0.30)
    while len(lista) < quantidade:
        valores = float(input('Insira os valores: '))
        if valores <= 1000:
            lista.append(valores)
        else:
            print('Insira novamente! Mas apenas valores entre 0 e 1000.')
    menor = min(lista)
    maior = max(lista)
    soma = sum(lista)
    print('######### Os resultados sao: #########')
    print(f'Maior valor: {maior}')
    print(f'Menor valor: {menor}')
    print(f'Soma: {soma}')


valores()
