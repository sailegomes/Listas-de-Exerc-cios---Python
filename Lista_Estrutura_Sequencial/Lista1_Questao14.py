def calculadora_valor_peso():
  peso_peixe = input('Qual é o peso do peixe? ')
  peso_peixe = float(peso_peixe)
  excesso = round(peso_peixe - 50,2)
  valor_a_pagar = round(excesso*4,3)
  if(excesso <=0):
    print('Parabéns! O peso do peixe pescado está dentro do permitido de acordo com o regulamento de pesca do estado de São Paulo.')
    print('uhh...')
    print('Mas...na minha opinião. Isso tá errado ok? Ninguém deveria pagar a mais por causa do peso do peixe que VOCÊ mesmo pescou. Tenha um ótimo dia!')
  else:
    print(f'Lamento, mas você deve pagar o excesso de {excesso} Kg. O valor a ser pago é de R${valor_a_pagar}')
    
calculadora_valor_peso()
