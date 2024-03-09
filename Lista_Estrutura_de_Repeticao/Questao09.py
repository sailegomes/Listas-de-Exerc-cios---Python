#Questao 9

# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time


lista_impar=[]
lista_par=[]
for i in range(1,51):
    if i%2 != 0:
        lista_impar.append(i)
    else:
        lista_par.append(i)
for i in lista_impar:
    print(i, end='')
    print(', ' if i != lista_impar[24] else '.', end='')

 

