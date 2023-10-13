def fruteira(morango,maca):
    morango = float(morango)
    maca = float(maca)
    peso_total = morango + maca
    if (peso_total <= 5):
        preco_morango = 2.50*morango
        preco_maca = 1.80*maca
        preco_total = preco_morango + preco_maca
        print(f'O preço a ser pago é de R${preco_total}. ')
    elif (peso_total > 5) and (peso_total < 8):
        preco_morango = 2.20*morango
        preco_maca = 1.50*maca
        preco_total = preco_morango + preco_maca
        print(f'O preço a ser pago é de R${preco_total}. ')
    elif (peso_total >= 8) or (preco_total > 25):
        preco_morango = 2.20*morango
        preco_maca = 1.50*maca
        preco_total = round((preco_morango + preco_maca),2)
        preco_total_desconto = 0.90*preco_total
        print(f'O preço a ser pago é de R${preco_total_desconto}. ')


fruteira(50,65)
