#Questao 24

# Faça um programa que calcule o mostre a média aritmética de N notas.

import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time

print(Fore.CYAN + 'Bem-vindo(a) ao TeacherAPP' + Fore.RESET)
qtde = int(input('Quantas notas você, professor(a), gostaria de inserir? '))
notas = []
while len(notas) < qtde:
    nota = float(input('Insira as notas: '))
    notas.append(nota)
media = round(sum(notas)/len(notas),2)
print(f'A média das notas do aluno(a) é: {media} ')
if media < 7:
    print(Fore.RED + 'Aluno(a) REPROVADO!!!! É uma pena, querido aluno. Torcemos pelo seu sucesso.' + Fore.RESET)
else:
    print(Fore.BLUE + 'Aluno(a) APROVADO!!!! Parabéns, querido aluno. Continue sempre assim!' + Fore.RESET)
