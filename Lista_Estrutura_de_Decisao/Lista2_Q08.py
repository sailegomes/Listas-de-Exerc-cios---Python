def melhor_compra():
    a = input('\n Dear user, insert the value of the first product: ')
    a = float(a)
    b = input('\n Dear user, insert the value of the next product: ')
    b = float(b)
    c = input('\n Dear user, insert the value of the last product: ')
    c = float(c)
    elif (a > b) and (a > c):
        print(f'\n You must buy the product with value U${a}.')
    elif (b > a) and (b > c):
        print(f'\n You must buy the product with value U${b}.')
    else:
        print(f'\n You must buy the product with value de U${c} dollars.')
    print(f' Thanks for use the our services. Have a nice day!')

melhor_compra()
