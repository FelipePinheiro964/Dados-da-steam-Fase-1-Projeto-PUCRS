##
# Classes de arquivos
##

## Carregar dados csv:

class Carregador_de_dados:
  def __init__(self, dados_csv):
    self.dados_csv = dados_csv

  def carregar_dados(self):
    try: #validação dos dados
      f = open(CSV, "r") #abrir dados em leitura
      print("dados carregados")

    except FileNotFoundError: # Notificar erro
      print("Erro ao carregar dados.")
      print("Programa finalizado, tente novamente.")
      raise SystemExit

dados_csv = 'steam_games.csv' #Nome do arquivo
carregador = Carregador_de_dados(dados_csv)

################################################