#Questao 37

# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final 
# da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser 
# informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e 
# dos pesos dos clientes

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

print(Fore.YELLOW + 'BEM-VINDO(A) AO REINO DAS GYM 👑' + Fore.RESET)
codigos = []
alturas = []
pesos = []
codigo = 1
while codigo != '0':
    codigo = str(input('Qual seu codigo de cadastro? '))
    if codigo == '0':
        break
    altura = float(input('Qual sua altura? '))
    peso = float(input('Qual seu peso? '))
    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)
time.sleep(0.35)
print('###### RESULTADOS ######')
print('')
time.sleep(0.33)
print(f'Sobre o cliente mais alto >>>',end='') 
print(f' Codigo:',end='') 
print(f'{codigos[alturas.index(max(alturas))]}'.zfill(4),end='') 
print(f' | Altura: {max(alturas)} m | Peso: {pesos[alturas.index(max(alturas))]} Kg ')
time.sleep(0.33)
print(f'Sobre o cliente mais baixo >>>',end='') 
print(f' Codigo:',end='') 
print(f'{codigos[alturas.index(min(alturas))]}'.zfill(4),end='') 
print(f' | Altura: {min(alturas)} m | Peso: {pesos[alturas.index(min(alturas))]} Kg ')
time.sleep(0.33)
print(f'Sobre o cliente mais gordo >>>',end='') 
print(f' Codigo:',end='') 
print(f'{codigos[pesos.index(max(pesos))]}'.zfill(4),end='') 
print(f' | Altura: {alturas[pesos.index(max(pesos))]} m | Peso: {max(pesos)} Kg ')
time.sleep(0.33)
print(f'Sobre o cliente mais magro >>>',end='') 
print(f' Codigo:',end='') 
print(f'{codigos[pesos.index(min(pesos))]}'.zfill(4),end='') 
print(f' | Altura: {alturas[pesos.index(min(pesos))]} m | Peso: {min(pesos)} Kg ')
time.sleep(0.33)
print(f'Media das alturas: {round(np.mean(alturas),2)} m')
time.sleep(0.33)
print(f'Media dos pesos: {round(np.mean(pesos),2)} kg')
