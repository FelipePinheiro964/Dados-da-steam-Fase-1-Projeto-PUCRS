##
# inicio de sistema
##


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
      count = 0
      for line in f: # ler suas linhas
        linhas = line.strip().split(',')
        count = count + 1
        print(linhas)
        if count == 100:
          break
        #print(linhas)  # imprimir todas as linhas, sem formatação, mas pode causar travamento


## Percentual de jogos pagos e gratuitos

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
      maior_avaliacao = 0
      nome_maior_avaliacao = 0
      next(f)
      for line in f: # ler suas linhas
        avaliacao = line.strip().split(',')[19]
        nome = line.strip().split(',')[1]
        if float(avaliacao) > maior_avaliacao:
            maior_avaliacao = avaliacao
            nome_maior_avaliacao = nome
        print(avaliacao)

