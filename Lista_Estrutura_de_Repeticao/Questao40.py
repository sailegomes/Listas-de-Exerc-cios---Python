#Questao 40

# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# a) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# b) Qual a média de veículos nas cinco cidades juntas;
# c) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

print(Fore.YELLOW + '🔥 BEM-VINDO(A) AO SISTEMA DE ACIDENTES DE TRABALHO 🔥' + Fore.RESET)
time.sleep(0.35)
print(Fore.BLUE + '######### CIDADES ALVOS DA COLETA DAS ESTATISTICAS #########' + Fore.RESET)
time.sleep(0.35)
print('Fortaleza CE - 85')
print('Boa Viagem CE - 88')
print('Sao Paulo (Capital) - 11')
print('Rio de Janeiro (Capital) - 21')
print('Teresina PI - 86')
print(Fore.RED + '##################################################' + Fore.RESET)
print('')
codigos,veiculos,acidentes = [],[],[]
a = 0
i = 0
while a < 5:
    a += 1
    codigo = str(input('Qual o codigo da cidade? '))
    codigos.append(codigo)
    veiculo = int(input(f'Qual o numero de veiculos em 1999 da cidade com codigo {codigos[i]}? '))
    veiculos.append(veiculo)
    acidente = int(input(f'Qual o numero de acidentes de transito com vitimas em 1999 da cidade com codigo {codigos[i]}? ')) 
    acidentes.append(acidente)
    i += 1
print(Fore.BLUE + '#### Menor e Maior Indice de Acidentes ####' + Fore.RESET)
time.sleep(0.50)
print(f'Menor indice de acidentes: {codigos[acidentes.index(min(acidentes))]} - {min(acidentes)}')
time.sleep(0.50)
print(f'Maior indice de acidentes: {codigos[acidentes.index(max(acidentes))]} - {max(acidentes)}')
time.sleep(0.35)
print('')
print(Fore.BLUE + '#### Media de Veiculos das 5 Cidades ####' + Fore.RESET)
time.sleep(0.35)
print(f'Media = {round(sum(veiculos)/5,2)} carros por cidade.')
time.sleep(0.35)
print('')
print(Fore.BLUE + '#### Media de Acidentes das Cidades com Menos de 2000 Veiculos ####' + Fore.RESET)
lista = []
for car in veiculos:
    if car < 2000:
        lista.append(car)
        print(f'Cidade {codigos[veiculos.index(car)]} com {car} veiculos')
print(f'Media = {sum(lista)/len(lista)}')
