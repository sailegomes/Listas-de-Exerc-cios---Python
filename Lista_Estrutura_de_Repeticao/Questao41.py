#Questao 41

# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, 
# quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25


# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

print(Fore.YELLOW + '🔥 BEM-VINDO(A) AO SISTEMA DE DIVIDAS 🔥' + Fore.RESET)
valor_inicial = float(input('Qual e o valor da divida do cliente? '))
parcelas = [1,3,6,9,12]
juros = [0,10,15,20,25]
valores = [] 
for i in juros:
    valor = valor_inicial + (i/100)*valor_inicial
    valores.append(valor)
print('Valor da Divida   Valor dos Juros   Qtde. de Parcelas   Valor da Parcela')
a = 0
for valor in valores:
    print(f'R${valor}', end = '')
    print(f'          R${str(valor - valor_inicial):<10}', end='')
    print(f'      {str(parcelas[a]):<10}', end='')
    print(f'          R${str(round(valor/parcelas[a],2)):<10}')
    a += 1
    print('')
