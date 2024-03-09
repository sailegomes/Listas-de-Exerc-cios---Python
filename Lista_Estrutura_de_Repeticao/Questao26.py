#Questao 26

# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
# e ao final mostrar o número de votos de cada candidato.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time

print(Fore.BLUE + 'Bem-vindo(a) às Eleições 2024! Escolha sábiamente o presidente que nos guiará em rumo à um futuro brilhante.)' + Fore.RESET)
time.sleep(0.05)
print('#####  A lista de candidatos é a seguinte  #####')
time.sleep(0.50)
print('A - Eduardo Campos')
time.sleep(0.50)
print('B - Lule')
time.sleep(0.50)
print('C - Marina Silva')
time.sleep(0.50)
print('D - Ey Ey Ey Mael')
time.sleep(0.50)
qtde = int(input('Quantos eleitores são? '))
lista_eleitores,eduardo,lula,marina,eymael = [],[],[],[],[]
while len(lista_eleitores) < qtde:
    voto = input('Qual é o seu voto? ')
    lista_eleitores.append(voto)
    if voto == 'A':
        eduardo.append(voto)
    elif voto == 'B':
        lula.append(voto)
    elif voto == 'C':
        marina.append(voto)
    else:
        eymael.append(voto)
print('')
print('')
print('###### Resultados das eleições 2024 ######')
print('')
time.sleep(0.50)
print(f'Eduardo Campos - {len(eduardo)} votos ({round((len(eduardo)/qtde)*100,2)}%)')
time.sleep(0.30)
print(f'Lule - {len(lula)} votos ({round((len(lula)/qtde)*100,2)}%)')
time.sleep(0.30)
print(f'Marina Silva - {len(marina)} votos ({round((len(marina)/qtde)*100,2)}%)')
time.sleep(0.30)
print(f'Ey Ey Ey Mael - {len(eymael)} votos ({round((len(eymael)/qtde)*100,2)}%)')
time.sleep(0.30)
