def tempo_download():
  tamanho = input('Qual o tamanho(em MB) do arquivo? ')
  tamanho = float(tamanho)
  velocidade = input('Qual a velocidade(em Mbps) do link de Internet? ')
  velocidade = float(velocidade)
  tempo = round(tamanho/velocidade,2)
  print(f'O tempo para baixar o arquvio de {tamanho} MB é de {tempo}s.')

tempo_download()
