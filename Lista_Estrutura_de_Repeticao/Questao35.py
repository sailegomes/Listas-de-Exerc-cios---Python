#Questao 35

# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 
# e um número inteiro informado pelo usuário.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math

# Esta função serve para identificar se o número inteiro é primo ou não.
def primo(numero):
    while numero == 1 or numero < 0:
        print('Digite outro numero, cegonha.')
        numero = int(input('Por favor, digite um numero inteiro qualquer: '))
    if numero == 3 or numero == 5 or numero == 7:
        resultado = True
        return(resultado)
    else:
        lista = []
        for i in range(2,10):
            resto = numero%i
            lista.append(resto)
        produto = 1
        for valores in lista:
            produto *= valores
        if produto == 0:
            resultado = False
            return(resultado)
        else:
            resultado = True
            return(resultado)
        


print(Fore.BLUE + 'Bem-vindo(a) ao PrimoAPP!' + Fore.RESET)
time.sleep(0.05)
numero = int(input('Digite um número inteiro qualquer: '))
print(f'\n Os números compreendidos em 1 a {numero} são: ', end = '')
lista = []
for i in range(1,numero+1):
    print(i, end = '')
    print(', ' if i < max(range(1,numero+1)) else '.', end = '')
    lista.append(i)
lista_primos = []
lista.remove(1)
for valor in lista:
    resultado = primo(valor)
    if resultado == True:
        lista_primos.append(valor)
print('\n Os números primos são: ', end = '')
for m in lista_primos:
    print(m, end = '')
    print(', ' if m < max(lista_primos) else '.', end='')
