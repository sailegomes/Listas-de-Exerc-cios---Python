# 44) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
# 1 , 2, 3, 4  - Votos para os respectivos candidatos 
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

import pandas as pd
import math
import numpy as np
from colorama import Fore
from time import sleep

print(Fore.YELLOW + '######### Bem-vindo(a) as Eleicoes 2024! Vote consciente! (┬┬﹏┬┬) #########' + Fore.RESET)
sleep(0.56)
print('----- Candidatos -----')
print('1 - Jose')
print('2 - Joao')
print('3 - Gabriel')
print('4 - Gustavo')
print('5 - Voto Nulo')
print('6 - Voto em Branco')
sleep(0.50)
voto = 1
votos1,votos2,votos3,votos4,votos5,votos6 = [],[],[],[],[],[]
while voto != 0:
    voto = int(input('Para qual candidato ira seu voto? '))
    if voto == 0:
        print('O programa sera encerrado! Todos os votos foram computados, obrigado! ')
        break
    elif voto == 1:
        votos1.append(voto)
    elif voto == 2:
        votos2.append(voto)
    elif voto == 3:
        votos3.append(voto)
    elif voto == 4:
        votos4.append(voto)
    elif voto == 5:
        votos5.append(voto)
    elif voto == 6:
        votos6.append(voto)
sleep(0.60)
votos_total = len(votos1)+len(votos2)+len(votos3)+len(votos4)+len(votos5)+len(votos6)
p1,p2,p3,p4,p5,p6 = round(len(votos1)/votos_total,2),len(votos2)/votos_total,len(votos3)/votos_total,len(votos4)/votos_total,len(votos5)/votos_total,len(votos6)/votos_total
candidatos = pd.DataFrame({'Candidatos':['Jose Magalhaes','Joao Alberto','Gabriel Angelim','Gustavo Mota','Voto Nulo','Voto em Branco','Total'],
                           'Quantidade de Votos':[len(votos1),len(votos2),len(votos3),len(votos4),len(votos5),len(votos6),votos_total],
                           'Porcentagens (%)':[p1,p2,p3,p4,p5,p6,p1+p2+p3+p4+p5+p6]})
candidatos.style.set_caption('RESULTADOS')
