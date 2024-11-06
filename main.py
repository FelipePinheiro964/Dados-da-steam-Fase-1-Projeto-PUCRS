##
# inicio de sistema
##


f = open("steam_games.csv", "r") #abrir dados em leitura


for line in f: # ler suas linhas
  linhas = line.strip().split(',') # variavel linhas para facilitar leitura
  #corrigido leitura defeituosa, mudança de ";" para ","
  print(linhas) # imprimir todas as linhas, sem formatação, mas pode causar travamento


f.close() # fecha o arquivo