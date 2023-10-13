def salario():
    salario = input('Quanto é o seu salário? ')
    salario = float(salario)
    if salario <= 280:
        aumento_20 = salario*1.20
        valor_aumentado20 = salario*0.20
        print(f'\n O seu salário antes do reajuste era de: R${salario}')
        print(' O percentual aplicado foi de 20%.')
        print(f'Valor do aumento: R${valor_aumentado20}')
        print(f'Seu novo salário é de: R${aumento_20}')
    elif (salario > 280) and (salario < 700):
        aumento_15 = salario*1.15
        valor_aumentado15 = salario*0.15
        print(f'\n O seu salário antes do reajuste era de: R${salario}')
        print('\n O percentual aplicado foi de 15%.')
        print(f'\n Valor do aumento: R${valor_aumentado15}')
        print(f'\n Seu novo salário é de: R${aumento_15}')
    elif (salario >= 700) and (salario < 1500):
        aumento_10 = salario*1.10
        valor_aumentado10 = salario*0.10
        print(f'\n O seu salário antes do reajuste era de: R${salario}')
        print('\n O percentual aplicado foi de 10%.')
        print(f'\n Valor do aumento: R${valor_aumentado10}')
        print(f'\n Seu novo salário é de: R${aumento_10}')
    else:
        aumento_05 = salario*1.05
        valor_aumentado05 = salario*0.05
        print(f'\n O seu salário antes do reajuste era de: R${salario}')
        print('\n O percentual aplicado foi de 5%.')
        print(f'\n Valor do aumento: R${valor_aumentado05}')
        print(f'\n Seu novo salário é de: R${aumento_05}')

salario()
