#Questao 25

# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma 
# varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time


print(Fore.BLUE + 'Bem-vindo(a)! Siga as instruções e bom proveito :)' + Fore.RESET)
qtde = int(input('Quantas pessoas são? '))
lista = []
while len(lista) < qtde:
    idade = int(input(f'Insira a idade das {qtde} pessoas: '))
    lista.append(idade)
media_idades = sum(lista)/len(lista)
if media_idades <= 25:
    print('O grupo de pessoas é', end='')
    print(Fore.BLUE + ' JOVEM' + Fore.RESET, end='')
    print('!')
elif media_idades >= 26 and media_idades <= 60:
    print('O grupo de pessoas é', end='')
    print(Fore.YELLOW + ' ADULTO' + Fore.RESET, end='')
    print('!')
else:
    print('O grupo de pessoas é', end='')
    print(Fore.RED + ' IDOSO' + Fore.RESET, end='')
    print('!')
