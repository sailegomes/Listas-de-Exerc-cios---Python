#Questao 27

# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a 
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math


print(Fore.BLUE + 'Olá! Bem-vindo(a) ao Cálculo De Turmas perefeito para sua instituição de ensino!' + Fore.RESET)
print('')
turmas = int(input('Quantas turmas são? '))
alunos = int(input('Quantos alunos são? '))
media = alunos/turmas
while media > 40:
    print(Fore.RED + 'Alguma turma ficará com mais de 40 alunos, por favor remanejar seus alunos e tente novamente!' + Fore.RESET)
    turmas = int(input('Quantas turmas são? '))
    alunos = int(input('Quantos alunos são? '))
    media_nova = alunos/turmas
    media = media_nova
    time.sleep(0.60)
time.sleep(0.60)
print(f'Sua instituição de ensino possui em média {math.floor(media)} alunos por turma.')
