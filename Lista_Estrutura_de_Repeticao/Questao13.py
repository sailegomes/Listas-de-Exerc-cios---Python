#Questao 13

# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

import pandas as pd
import numpy as np
from colorama import Fore, Back, Style
import time


def potencia():
    print(Fore.YELLOW + 'Hello! Welcome to calculator of potency 🔥🔥🔥' + Fore.RESET)
    base = int(input('Digite o valor da base: '))
    expoente = int(input('Digite o valor do expoente: '))
    valor = base**expoente
    print(Fore.BLUE + f'Resultado -> {valor}' + Fore.RESET)

potencia()
    
