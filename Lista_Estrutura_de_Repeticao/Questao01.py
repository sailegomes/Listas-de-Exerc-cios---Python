#Questao 1
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido continue pedindo até que o 
# usuário informe um valor válido.

def nota():
    nota = float(input('\n Insira um nota de 0 a 10: '))
    while nota < 0 or nota > 10:
        print('\n Eu sei que voce esta digitando um nota fora do intervalo '
              'solicitado! Por favor, inserir uma nota conforme solicitado.')
        nota = float(input('\n Insira um nota de 0 a 10: '))
    print('\n Nota registrada com sucesso! Origado, caro usuario :)')

nota()
