#Questao 31

# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido 
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final
# da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
# então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
# a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara 
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...


import pandas as pd
import numpy as np 
from colorama import Fore, Back, Style
import time
import math


print(Fore.BLUE + '🔥🔥🔥  Bem-vindo(a) às Lojas Tabajara  🔥🔥🔥' + Fore.RESET)
time.sleep(0.50)
print('Lojas Tabajara')
valores = []
valor = 1
while valor != 0:
    valor = float(input('Insira o valor do produto: '))
    valores.append(valor)
a = 0
for i in range(1,len(valores)):
    print(f'Produto {i}: R${valores[a]}')
    a += 1
time.sleep(0.30)
print(f'Total: R${sum(valores)}')
time.sleep(0.30)
dinheiro = float(input('Dinheiro do cliente: '))
print(f'Dinheiro: R${dinheiro}')
time.sleep(0.30)
print(f'Troco: R${round(dinheiro-sum(valores),2)}')
