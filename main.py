##
# inicio de sistema
##

import csv

try: #validação dos dados
   f = open("steam_games.csv", "r") #abrir dados em leitura
   print("dados carregados")

except FileNotFoundError: # Notificar erro
    print("Erro ao carregar dados.")
    print("Programa finalizado, tente novamente.")
    raise SystemExit


# Iniciar loop do sistema
while True:
  entrada = input("selecione o numero:")#Selecionar questão/função
  entrada = entrada.lower()

  if entrada == 'sair':
    print("Programa finalizado")
    break
  else:
    if not entrada.isdigit():
      print("Entrada invalida")
      continue
    else:
      entrada = int(entrada)

##
# Operações do sistema
##

 # Imprimir todo o arquivo
  match entrada:

    case 1:
      count = int(input('Quantas linhas deseja visualizar: '))
      freio = 0
      for line in f: # ler suas linhas
         freio = freio + 1
         linhas = line.strip().split(',')
         print(linhas)
         if freio == count:
           break
        #print(linhas)  # imprimir todas as linhas, sem formatação, mas pode causar travamento


## questão 1 Percentual de jogos pagos e gratuitos

    case 2:
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



##
#    Questão 3: jogo com melhor avaliação do usuario
##


    case 4:
      #arquivo
      arquivo_csv = 'steam_games.csv'


      preco = 0
      nome_jogo = ''

      with open(arquivo_csv, 'r') as arquivo:
        steam_dados = csv.reader(arquivo, delimiter = ',', quotechar = '"') # delimitador
        cabecalho = next(arquivo) # Cabecalho
        print(cabecalho[1:6]) 
        for linha in steam_dados:
          try:
            if float(linha[6]) > preco:
              print(linha[6])
              preco = float(linha[6])
              nome_jogo = linha[1]
          except:
            ValueError
            continue

      print(f'O jogo mais caro da steam é {nome_jogo}, e custa {preco} dolares!!!')



