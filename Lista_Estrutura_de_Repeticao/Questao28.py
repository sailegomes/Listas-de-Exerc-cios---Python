#Questao 28

# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor 
# médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

print(Fore.BLUE + "Olá! Bem-vindo(a) ao CD's APP!" + Fore.RESET)
print('')
cds = int(input("Quantos CD's você possui? "))
valores = []
while len(valores) < cds:
    valor = float(input("Insira os valores de cada um dos CD's comprados:" ))
    valores.append(valor)
total_investido = sum(valores)
media = round(total_investido/cds,2)
print(f'O total investido foi de: R${total_investido} ')
print(f'O valor gasto em média por CD foi de: R${media}')
