#Questao 3
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
from colorama import Fore, Back, Style

def cadastro():
    print('Ola! Seja muito bem vindo ao sistema de cadastro nacional de pessoas fisicas.')
    print('Para iniciar, preencha as informacoes necessarias abaixo.')
    nome = input('Nome: ')
    while len(nome) < 3: 
        print(Fore.RED + 'ERRO! Digite um nome valido!')
        nome = input('Nome: ')
    idade = int(input('Idade: '))
    while idade < 3 or idade > 150: 
        print(Fore.RED + 'ERRO! Digite uma idade valida!')
        idade = input('Idade: ')
    salario = float(input('Salario: '))
    while salario < 0: 
        print(Fore.RED + 'ERRO! Digite um salario valido!')
        salario = float(input('Salario: '))
    genero = input('Genero (f/m): ')
    while genero != 'm' and genero != 'f': 
        print(Fore.RED + 'ERRO! Digite um genero valido!')
        genero = input('Genero (f/m): ')
    estado_civil = input('Estado Civil (s/c/v/d): ')
    while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd': 
        print(Fore.RED + 'ERRO! Digite um Estado Civil valido!')
        estado_civil = input('Estado Civil (s/c/v/d): ')
    print(Fore.BLUE + 'PARABENS! Dados cadastrados com sucesso.')

cadastro()
