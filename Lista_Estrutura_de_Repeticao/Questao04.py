#Questao 4

# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a 
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
# de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
from colorama import Fore, Back, Style
import time

def populacao():
    popA = int(input('\n Insira o numero de habitantes da populacao A: '))
    popB = int(input('\n Insira o numero de habitantes da populacao B: '))
    print(Fore.BLUE + 'Numero de habitantes cadastrados com sucesso. 👍' + Fore.RESET)
    taxaA = float(input('\n Insira a taxa de crescimento anual da populacao A: '))
    taxaB = float(input('\n Insira a taxa de crescimento anual da populacao B: '))
    time.sleep(0.60)
    print(Fore.BLUE + 'Taxas de crescimento anuais dos habitantes cadastradas com sucesso. 👍' + Fore.RESET)
    i = 0
    while popA != popB:
        popA *= (taxaA/100)
        popB *= (taxaB/100)
        i += 1
    time.sleep(0.60)
    print(f'A quantidade de anos para que a populacao A alcance a populacao B e de {i} anos.')


populacao()
