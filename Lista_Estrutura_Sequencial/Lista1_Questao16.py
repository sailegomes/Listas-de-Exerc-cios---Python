def tintas_ltda():
  import math
  tam = input('Quanto mede, em m², a área que será pintada? ')
  tam = float(tam)
  litros_necessarios = tam/3
  numero_latas = math.floor(litros_necessarios/18)
  preco_latas = 80 * numero_latas
  print(f'Quantidade necessária de lata(s) de tinta: {numero_latas}')
  print(f'Preço total de {numero_latas} lata(s) de tinta: R${preco_latas}')

tintas_ltda()
