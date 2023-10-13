def combustiveis():
    combustivel = input('\n Qual é o combustível desejado (gasolina/alcool)? ')
    litros = float(input('\n Quantos litros serão colocados? '))
    preco_alcool_menor_20L = (1.90*litros)-(1.90*litros*0.03)
    preco_alcool_maior_20L = (1.90*litros)-(1.90*litros*0.05)
    preco_gasolina_menor_20L = (2.50*litros)-(2.50*litros*0.04)
    preco_gasolina_maior_20L = (2.50*litros)-(2.50*litros*0.06)
    if (combustivel == 'alcool') and (litros <= 20):
        print(f'\n O combustível escolhido foi Álcool, e seu preço por litro é de R$1,90. O preço a ser pago será '
              f'R${preco_alcool_menor_20L} por {litros} litros de Álcool.')
    elif (combustivel == 'alcool') and (litros > 20):
        print(f'\n O combustível escolhido foi Álcool, e seu preço por litro é de R$1,90. O preço a ser pago será '
              f'R${preco_alcool_maior_20L} por {litros} litros de Álcool.')
    elif (combustivel == 'gasolina') and (litros <= 20):
        print(f'\n O combustível escolhido foi Gasolina, e seu preço por litro é de R$2,50. O preço a ser pago será '
              f'R${preco_gasolina_menor_20L} por {litros} litros de Gasolina.')
    elif (combustivel == 'gasolina') and (litros > 20):
        print(f'\n O combustível escolhido foi Gasolina, e seu preço por litro é de R$2,50. O preço a ser pago será '
              f'R${preco_gasolina_maior_20L} por {litros} litros de Gasolina.')


combustiveis()
