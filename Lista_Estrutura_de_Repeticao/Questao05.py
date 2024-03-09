#Questao 5

# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

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
