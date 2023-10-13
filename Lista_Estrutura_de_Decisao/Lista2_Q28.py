def carnes():
    tipo = input('\n Qual o tipo de carne desejado (File Duplo/Alcatra/Picanha)?  ')
    peso = float(input('\n Qual a quantidade, em Kg, de carne? '))
    pagamento = input('\n Qual a forma de pagamento? ')
    if (tipo == 'File Duplo') and (peso <= 5):
        preco_file_duplo = peso*4.90
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_file_duplo} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: SEM DESCONTO '
              f'\n Valor a pagar: R${preco_file_duplo} ')
    if (tipo == 'Alcatra') and (peso <= 5):
        preco_alcatra = peso*5.90
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_alcatra} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: SEM DESCONTO '
              f'\n Valor a pagar: R${preco_alcatra} ')
    if (tipo == 'Picanha') and (peso <= 5):
        preco_picanha = peso*6.90
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_picanha} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: SEM DESCONTO '
              f'\n Valor a pagar: R${preco_picanha} ')
    if (tipo == 'File Duplo') and (peso > 5):
        preco_file_duplo = peso*5.80
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_file_duplo} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: SEM DESCONTO '
              f'\n Valor a pagar: R${preco_file_duplo} ')
    if (tipo == 'Alcatra') and (peso > 5):
        preco_alcatra = peso*6.80
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_alcatra} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: SEM DESCONTO '
              f'\n Valor a pagar: R${preco_alcatra} ')
    if (tipo == 'Picanha') and (peso > 5):
        preco_picanha = peso*7.80
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_picanha} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: SEM DESCONTO '
              f'\n Valor a pagar: R${preco_picanha}')

    if (tipo == 'File Duplo') and (peso <= 5) and (pagamento == 'cartão Tabajara'):
        preco_file_duplo = peso*4.90
        desconto = preco_file_duplo*0.05
        valor_pagar = preco_file_duplo - desconto
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_file_duplo} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: R${desconto} '
              f'\n Valor a pagar: R${valor_pagar}')
    if (tipo == 'Alcatra') and (peso <= 5) and (pagamento == 'cartão Tabajara'):
        preco_alcatra = peso*5.90
        desconto = preco_alcatra*0.05
        valor_pagar = preco_alcatra - desconto
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_alcatra} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto R${desconto}: '
              f'\n Valor a pagar: R${valor_pagar} ')
    if (tipo == 'Picanha') and (peso <= 5) and (pagamento == 'cartão Tabajara'):
        preco_picanha = peso*6.90
        desconto = preco_picanha*0.05
        valor_pagar = preco_picanha - desconto
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_picanha} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: R${desconto} '
              f'\n Valor a pagar: R${valor_pagar} ')
    if (tipo == 'File Duplo') and (peso > 5) and (pagamento == 'cartão Tabajara'):
        preco_file_duplo = peso*5.80
        desconto = preco_file_duplo*0.05
        valor_pagar = preco_file_duplo - desconto
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_file_duplo} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: R${desconto} '
              f'\n Valor a pagar: R${valor_pagar} ')
    if (tipo == 'Alcatra') and (peso > 5) and (pagamento == 'cartão Tabajara'):
        preco_alcatra = peso*6.80
        desconto = preco_alcatra*0.05
        valor_pagar = preco_alcatra - desconto
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_alcatra} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: R${desconto} '
              f'\n Valor a pagar: R${valor_pagar} ')
    if (tipo == 'Picanha') and (peso > 5) and (pagamento == 'cartão Tabajara'):
        preco_picanha = peso*7.80
        desconto = preco_picanha*0.05
        valor_pagar = preco_picanha - desconto
        print(f'\n ------CUPOM FISCAL------'
              f'\n Tipo da carne: {tipo} '
              f'\n Quantidade comprada: {peso} Kg '
              f'\n Preço total: R${preco_picanha} '
              f'\n Tipo de pagamento: {pagamento} '
              f'\n Valor do desconto: R${desconto} '
              f'\n Valor a pagar: R${valor_pagar} ')

carnes()
