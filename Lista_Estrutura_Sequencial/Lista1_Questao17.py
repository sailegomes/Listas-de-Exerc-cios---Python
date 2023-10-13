def tintas_ltda():
  import math
  tam = input('Quanto mede, em m², a área que será pintada? ')
  tipo = input('As tintas serão em latas(1) ou galões(2)? ')
  tam = float(tam)
  tipo = int(tipo)
  litros_necessarios = round(tam/6,2)
  numero_latas_18 = math.floor(litros_necessarios/18)
  numero_galoes_36 = math.floor(litros_necessarios/3.6)
  preco_latas_18 = 80 * numero_latas_18
  preco_galoes_36 = 25 * numero_galoes_36
  if(tipo == 1):
    print(f'Quantidade necessária de lata(s) de tinta: {numero_latas_18}')
    print(f'Preço total de {numero_latas_18} lata(s) de tinta: R${preco_latas_18}')
  else:
    print(f'Quantidade necessária de galão(ões) de tinta: {numero_galoes_36}')
    print(f'Preço total de {numero_galoes_36} galão(ões) de tinta: R${preco_galoes_36}')


tintas_ltda()
