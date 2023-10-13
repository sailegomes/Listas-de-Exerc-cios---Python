def dia_semana():
   dia = input('\n Digite um número e obtenha um dia da semana: ')
   dia = int(dia)
   if dia == 1:
       print('\n Domingo.')
   elif dia == 2:
       print('\n Segunda.')
   elif dia == 3:
       print('\n Terça.')
   elif dia == 4:
       print('\n Quarta.')
   elif dia == 5:
       print('\n Quinta.')
   elif dia == 6:
       print('\n Sexta.')
   elif dia == 7:
       print('\n Sábado.')
   else:
       print('\n Valor inválido. Digite outro número, por favor.')


dia_semana()
