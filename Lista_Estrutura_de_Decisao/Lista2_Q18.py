def data():
    print('\n Por favor, digite uma data no formato dd/mm/aaaa. ')
    dia = input('\n Dia: ')
    dia = int(dia)
    mes = input('\n Mês: ')
    mes = int(mes)
    ano = input('\n Ano: ')
    ano = int(ano)
    dat = date(ano,mes,dia)
    dat2 = dat.strftime('%d/%m/%y')
    print(f'\n A data inserida foi {dat2}. É uma data válida.')

data()
