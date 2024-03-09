#Questao 38

# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# a) Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# b) Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# c) A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do 
#    percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. 
#    Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.


import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math


def salary():
    print(Fore.YELLOW + '🔥 BEM-VINDO(A) AO SALARY 2K24 🔥' + Fore.RESET)
    salario = 1000
    taxa = 0.015
    time.sleep(0.35)
    print(f'Salario inicial: R$1000,00 em 1995')
    for i in range(1,29):
        ano = 1994 + i
        aux = ano
        print(f'{aux}: R${round(salario,2)} | taxa: {taxa*100}%')
        salario *= (1 + taxa) 
        taxa *= 2
        time.sleep(0.30)


def salary2():
    print(Fore.YELLOW + '🔥 BEM-VINDO(A) AO SALARY 2K24 2.0 🔥' + Fore.RESET)
    salario = float(input('Qual o salário inicial? '))
    time.sleep(0.35)
    ano_inicial = int(input('Qual o ano de início? '))
    ano_final = int(input('Qual o ano de fim? '))
    taxa = float(input('Qual a taxa anual de aumento de salário? '))
    time.sleep(0.35)
    print(f'Salario inicial: R${salario} em 1995')
    for i in range(1,ano_final-ano_inicial+2):
        ano = ano_inicial -1 + i
        aux = ano
        print(f'{aux}: R${round(salario,2)} | taxa: {taxa*100}%')
        salario *= (1 + taxa) 
        taxa *= 2
        time.sleep(0.30)

salary2()
