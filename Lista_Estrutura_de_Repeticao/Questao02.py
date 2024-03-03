#Questao 2
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
# de erro e voltando a pedir as informações.

def login():
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    while usuario == senha:
        print('Ola! Nao e possivel cadastrar um login onde o nome de usuario e senha sao iguais! Por favor, altere sua senha ou'
              'altere seu nome de usuario.')
        usuario = input('Usuario: ')
        senha = input('Senha: ')
    print('Login cadastrado com sucesso! Seja muito bem vindo(a) ao nosso universo magnifico! Enjoy!')

login()

