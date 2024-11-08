##
# Classes de arquivos
##

## Carregar dados csv:

class Carregador_de_dados:  
  def __init__(self, dados_csv):  
      self.dados_csv = dados_csv  # Atributo da instância  

  def carregar_dados(self):  
      try:  # Validação dos dados  
          with open(self.dados_csv, "r") as f:  # Abrir dados em leitura  
              next(f)
              print("Dados carregados")  
              return f.readlines()  # Retorna as linhas do arquivo  

      except FileNotFoundError:  # Notificar erro  
          print("Erro ao carregar dados.")  
          print("Programa finalizado, tente novamente.")  
          raise SystemExit  
################################################