#Questao 30

# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
# sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de
# 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

print(Fore.BLUE + '🔥🔥🔥  Bem-vindo(a) à tabela de preços PANIFICADORA PÃO DE ONTEM  🔥🔥🔥' + Fore.RESET)
time.sleep(0.50)
print('Preço do pão: R$0,18 ')
print('Panificadora Pão de Ontem - Tabela de preços ')
print('')
for i in range(1,51):
    print(i,end='')
    print(f' - R${round(i*0.18,2)}')
    time.sleep(0.30)
