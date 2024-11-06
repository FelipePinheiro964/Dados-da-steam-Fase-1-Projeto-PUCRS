##
# inicio de sistema
##
entrada = int(input("selecione o numero:"))#abrir dados em leitura


f = open("steam_games.csv", "r") #abrir dados em leitura

linhas = line.strip().split(',') # variavel linhas para facilitar leitura

if entrada == 1:
  for line in f: # ler suas linhas
    linhas = line.strip().split(',')
    #corrigido leitura defeituosa, mudança de ";" para ","
    print(linhas)  # imprimir todas as linhas, sem formatação, mas pode causar travamento


## Percentual de jogos pagos e gratuitos

gratis = 0

i = 0

if entrada == 2:
    for linha in f:
      if i < 10:
        if linhas[6] == "0":
          gratis += 1
          #print(linhas)


print(gratis)

f.close()# fecha o arquivo