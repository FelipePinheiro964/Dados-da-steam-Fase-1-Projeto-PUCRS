##
# inicio de sistema
##

try: #validação dos dados
   f = open("steam_games.csv", "r") #abrir dados em leitura
   print("dados carregados")
except FileNotFoundError: # Notificar erro
    print("Erro ao carregar dados.")

# Iniciar loop do sistema
while True: 
  entrada = int(input("selecione o numero:"))#Selecionar questão/função

##
# Operações do sistema
##

 # Imprimir todo o arquivo

  if entrada == 1:
    for line in f: # ler suas linhas
      linhas = line.strip().split(',')
      #print(linhas)  # imprimir todas as linhas, sem formatação, mas pode causar travamento


## Percentual de jogos pagos e gratuitos

  gratuito = 0
  pago = 0
  total_linhas = 0

  if entrada == 2:
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