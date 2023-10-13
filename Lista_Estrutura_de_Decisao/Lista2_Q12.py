def folha_pagamento():
    print('Olá, seja muito bem vindo ao PayCheck! Digite abaixo as informações pedidas.')
    horas = input('Digite a quantidade de horas que você trabalho no mês: ')
    horas = float(horas)
    valor = input('Qual o valor da sua hora trabalhada? ')
    valor = float(valor)
    sal_bruto = horas * valor
    ir = 0.05*sal_bruto
    inss = 0.10*sal_bruto
    fgts = 0.11*sal_bruto
    desconto = ir + inss
    sal_liq = sal_bruto - desconto
    if sal_bruto <= 900:
        print(f'\n Salário bruto: R${sal_bruto}')
        print(f'\n IR (5%): R${ir}')
        print(f'\n INSS (10%): R${inss}')
        print(f'\n FGTS (11%): R${fgts}')
        print(f'\n Total de descontos: R${desconto}')
        print(f'\n Salário Líquido: R${sal_liq}')
    elif 900 < sal_bruto <=1500:
        print(f'\n Salário bruto: R${sal_bruto}')
        print(f'\n IR (5%): R${ir}')
        print(f'\n INSS (10%): R${inss}')
        print(f'\n FGTS (11%): R${fgts}')
        print(f'\n Total de descontos: R${desconto}')
        print(f'\n Salário Líquido: R${sal_liq}')
    elif 1500 < sal_bruto <= 2000:
        print(f'\n Salário bruto: R${sal_bruto}')
        print(f'\n IR (5%): R${ir}')
        print(f'\n INSS (10%): R${inss}')
        print(f'\n FGTS (11%): R${fgts}')
        print(f'\n Total de descontos: R${desconto}')
        print(f'\n Salário Líquido: R${sal_liq}')
    else:
        print(f'\n Salário bruto: R${sal_bruto}')
        print(f'\n IR (5%): R${ir}')
        print(f'\n INSS (10%): R${inss}')
        print(f'\n FGTS (11%): R${fgts}')
        print(f'\n Total de descontos: R${desconto}')
        print(f'\n Salário Líquido: R${sal_liq}')

folha_pagamento()
