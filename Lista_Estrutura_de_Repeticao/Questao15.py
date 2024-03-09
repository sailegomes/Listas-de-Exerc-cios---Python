#Questao 15

# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time


def fibonacci():
    print(Fore.BLUE + 'Seja muito bem-vindo(a) ao FIBONACCI APP. Seu gerador de sequencia de Fibonacci. 🔥🔥😁' + Fore.RESET)
    time.sleep(0.23)
    objetivo = int(input('Ate qual termo voce deseja gerar a sequencia de Fibonacci? '))
    primeiro = 1
    ultimo = 0
    lista = []
    for i in range(1,objetivo+1):
        lista.append(primeiro)
        a = primeiro
        primeiro += ultimo
        ultimo = a
    for valor in lista:
        print(valor, end = '')
        print(', ' if valor != max(sorted(lista)) else '.', end = '' )
        time.sleep(0.56)

fibonacci()     
