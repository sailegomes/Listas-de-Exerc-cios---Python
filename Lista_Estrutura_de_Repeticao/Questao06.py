#Questao 6

# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa 
# para que ele mostre os números um ao lado do outro.


# Primeira parte do exercicio.
def numeros():
    for i in range(20):
        print(i+1)


# Segunda parte do exercicio.
def numeros2():
   for i in range(1,21):
    print(i, end = '')
    print(', ' if i < 20 else '.', end='')

