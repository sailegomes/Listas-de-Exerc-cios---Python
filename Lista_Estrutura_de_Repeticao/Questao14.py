#Questao 14

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time

def separador():
    lista = []
    print(Fore.GREEN + '#######' + Fore.RESET + ' Ola! Seja muito bem vindo, ao SEPARADOR DE NUMEROS ' + Fore.GREEN + '#######' + Fore.RESET)
    while len(lista) < 10:
        numero = int(input('Digite 10 numeros inteiros: '))
        lista.append(numero)
    lista_impar = []
    lista_par = []
    for i in lista:
        if i%2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    print(f'\n A seguir temos a lista de numeros pares, contendo {len(lista_par)} numeros. ')
    for par in sorted(lista_par):
        print(par, end = '')
        print(', ' if par != max(lista_par) else '.', end= '')
    print(f'\n A seguir temos a lista de numeros impares, contendo {len(lista_impar)} numeros. ')
    for impar in sorted(lista_impar):
        print(impar, end = '')
        print(', ' if impar != max(lista_impar) else '.', end = '')

separador()
