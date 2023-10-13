def triangle():
    ladoA = input('\n Qual o valor do lado A? ')
    ladoB = input('\n Qual o valor do lado B? ')
    ladoC = input('\n Qual o valor do lado C? ')
    ladoA = float(ladoA)
    ladoB = float(ladoB)
    ladoC = float(ladoC)
    if ((ladoA < ladoB + ladoC or ladoB < ladoA + ladoC or ladoC < ladoA + ladoB) and (ladoA == ladoB == ladoC)):
        print('\n Os valores informados formam um triângulo equilátero.')
    elif ((ladoA < ladoB + ladoC or ladoB < ladoA + ladoC or ladoC < ladoA + ladoB) and (ladoA == ladoB or ladoA == ladoC or ladoB == ladoC)):
        print('\n Os valores informados formam um triângulo isósceles.')
    elif ((ladoA < ladoB + ladoC or ladoB < ladoA + ladoC or ladoC < ladoA + ladoB) and (ladoA != ladoB != ladoC)):
        print('\n Os valores informados formam um triângulo escaleno.')
    else:
        print('\n Os valores informados não formam um triângulo.')

triangle()
