#Questao 36

# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve 
# necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:


# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math


def tabuada():
    print(Fore.YELLOW + 'BEM-VINDO(A) AO REI DA TABUADA! 👑' + Fore.RESET)
    time.sleep(0.010)
    numero = int(input('Qual numero voce desejar saber a tabuada?'))
    inicial = int(input('Por qual numero voce deseja começar?'))
    final = int(input('Por qual numero voce deseja terminar?'))
    while final < inicial:
        print('Você digitou o valor',end='')
        print(Fore.RED + ' FINAL ' + Fore.RESET,end='')
        print('maior do que o valor',end='')
        print(Fore.RED + ' INICIAL' + Fore.RESET,end='')
        print('! Por faovr, inserir novamente as informações.')
        inicial = int(input('Por qual numero voce deseja começar?'))
        final = int(input('Por qual numero voce deseja terminar?'))
    print(f'Montar a tabuada do: {numero}')
    print(f'Começar por: {inicial}')
    print(f'Terminar em: {final}')
    print('')
    print(f'Vou montar a tabuada de {numero} começando em {inicial} e terminando em {final}: ')
    for i in range(inicial,final+1):
         print(f'{numero}x{i} = {numero * i}')

tabuada()
