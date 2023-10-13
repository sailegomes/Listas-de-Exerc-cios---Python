def leitor(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    if(a> b) and (a> c):
        print(f'\n O {a} é o maior número. ')
    elif(b> a) and (b>c):
        print(f'\n O {b} é o maior número. ')
    elif(c> a) and (c>b):
        print(f'\n O {c} é o maior número. ')
    elif(a<b) and (a<c):
        print(f'\n O {a} é menor número.')
    elif(b<a) and (b<c):
        print(f'\n O {b} é menor número.')
    else:
        print(f'\n O {c} é menor número.')

leitor(4,5,6)
