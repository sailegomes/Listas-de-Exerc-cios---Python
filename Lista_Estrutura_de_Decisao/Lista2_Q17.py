def funcao_quadratica():
    print('Bem-vindo(a) à calculadora de função do 2º grau!')
    a = input('\n Insira o valor do coeficiente a: ')
    b = input('\n Insira o valor do coeficiente b: ')
    c = input('\n Insira o valor do coeficiente c: ')
    a = float(a)
    b = float(b)
    c = float(c)
    delta = b**2 - 4*a*c
    x1 = round((-b + delta**(1/2))/2*a,2)
    x2 = round((-b - delta**(1/2))/2*a,2)
    print(f'\n O formato da equação inserida é {a}x² + ({b})x + {(c)}.')
    if a == 0:
        print('\n A equação não é do segundo grau, e sim do primeiro grau. '
              'Lamento, mas o programa será encerrado!')
    elif delta < 0:
        print('\n O delta é negativo, e portanto não possui raízes reais. Para'
              'esta finalidade, recomendamos que o caro usuário experimente'
              'utilizar o conjunto dos números complexos. O programa será encerrado!')
    elif delta == 0:
        print('\n O delta é nulo, e portanto possui uma única raíz real.')
        print(f'\n A raíz da equação é igual a {x1}.')
    elif delta > 0:
        print('\n O delta é positivo, e portanto possui duas raízes reais.')
        print(f'\n As raízes da equação são iguais a {x1} e {x2}.')

funcao_quadratica()
