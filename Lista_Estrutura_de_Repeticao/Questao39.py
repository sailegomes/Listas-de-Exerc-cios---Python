#Questao 39

# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando
# a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno
# mais baixo, junto com suas alturas.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math


print(Fore.YELLOW + '🔥 BEM-VINDO(A) AO ALTURA 2000 🔥' + Fore.RESET)
numeros,alturas = [],[]
numero=1
while numero != 0:
    numero = int(input('Qual o código do aluno(a)? '))
    numeros.append(numero)
    if numero == 0:
        break
    altura = float(input('Qual a altura do aluno(a)? '))
    alturas.append(altura)
numeros.remove(0)
alto = max(alturas)
baixo = min(alturas)
time.sleep(0.35)
print(Fore.BLUE + 'Mais alto' + Fore.RESET, end='')
print(f' >>> Número: {numeros[alturas.index(alto)]}'.zfill(3), end = '')
print(f' | Altura: {alto} m')
print(Fore.RED + 'Mais baixo' + Fore.RESET, end='')
print(f' >>> Número: {numeros[alturas.index(baixo)]}'.zfill(3),end='')
print(f' | Altura: {baixo} m')
