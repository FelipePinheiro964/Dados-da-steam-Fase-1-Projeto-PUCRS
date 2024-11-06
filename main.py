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

gratuito = 0
pago = 0
total_linhas = 0


for line in f: # ler suas linhas
  preco = line.strip().split(',')[7]
  total_linhas = total_linhas + 1
  #print(preco)
  if preco == '0.0':
    gratuito = gratuito + 1
  else:
    pago = pago + 1

#print(gratuito, pago)
#print(total_linhas)

porcentagem_jogosgratuitos = (gratuito/total_linhas)*100
porcentagem_jogospagos = (pago/total_linhas)*100

print(f'% jogos gratuitos {porcentagem_jogosgratuitos:.2f}')
print(f'% jogos pagos {porcentagem_jogospagos:.2f}')

f.close()# fecha o arquivo