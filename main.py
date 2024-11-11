## Nome? Felipe Pinheiro Fossá
## Curso: Banco de dados: ênfase em data analytics
## Fase 1 - Projeto de programação para dados

import csv  

######################################################  
## Classe para carregar dados csv:  
######################################################  

class Carregador_de_dados:  
    def __init__(self, dados_csv):  
        self.dados_csv = dados_csv  # Atributo da instância  

    def carregar_dados(self):  
        try:  
            with open(self.dados_csv, "r", newline='') as f:  # Abrir dados em leitura  
                leitor = csv.reader(f)  
                next(leitor)  # Ignora o cabeçalho  
                print("Dados carregados")  
                return [linha for linha in leitor]  # Retorna as linhas como listas  

        except FileNotFoundError:  # Formatação de erro
            print("Erro ao carregar dados, nome ou arquivo não identificado.")  
            print("Programa finalizado, tente novamente.")  
            raise SystemExit  

#####################################################  
# Classe para utilizar o menu  
#####################################################  

class Menu:  
    def __init__(self, selecionar_opcao):  
        self.selecionar_opcao = selecionar_opcao  

    def opcoes(self, linhas_dados):  
        match self.selecionar_opcao:  
            case 1:  
                self.visualizar_linhas(linhas_dados)      ## Opções do menu
            case 2:  
                self.percentual_jogos(linhas_dados)  
            case 3:  
                self.data_mais_lancamentos(linhas_dados)  
            case 4:  
                self.jogo_mais_caro(linhas_dados)
            case _:  
                print('Opção não válida, selecione um numero descrito no menu.')  

#####################################################
# Definir funçao de visualizar linhas
#####################################################

    def visualizar_linhas(self, linhas_dados):  
        count = int(input('Quantas linhas deseja visualizar: '))  
        for freio, line in enumerate(linhas_dados, start=1):  
            print(line)  # A linha já é uma lista  
            if freio == count:  
                break  

#####################################################
# Definir funçao de percentual de jogos pagos e gratuitos
#####################################################

    def percentual_jogos(self, linhas_dados):  
        gratuito = 0  
        pago = 0  # Variáveis
        total_linhas = 0  

        for line in linhas_dados:  
            preco = line[6]  
            total_linhas += 1  
            
            if preco == '0.0':  
                gratuito += 1  
            else:  
                pago += 1  # Corrigido para "pago += 1, para otimizar programa"  

        if total_linhas > 0:  # Evita divisão por zero  
            porcentagem_jogosgratuitos = (gratuito / total_linhas) * 100  # Calculo de porcentagem
            porcentagem_jogospagos = (pago / total_linhas) * 100  

            print(f"% de jogos gratuitos: {porcentagem_jogosgratuitos:.2f}")  
            print(f"% de jogos pagos: {porcentagem_jogospagos:.2f}")  

#####################################################
# Definir funçao de ano com mais lançamentos
#####################################################

    def data_mais_lancamentos(self, linhas_dados):  
        contagem_datas = {}  # Lista para contagem

        for linha in linhas_dados:  
            data_lancamento = linha[2]  
            if data_lancamento in contagem_datas:  
                contagem_datas[data_lancamento] += 1  
            else:  # inicia um contagem dos anos e datas 
                contagem_datas[data_lancamento] = 1  

        if contagem_datas:  # Verifica se há dados  
            ano_mais_frequente = max(contagem_datas, key=contagem_datas.get)  
            print(f'O ano mais frequente de lançamentos é: {ano_mais_frequente[6:]}')  

#####################################################
# Definir função jogo mais caro do arquivo
#####################################################

    def jogo_mais_caro(self, linhas_dados):  
        preco = 0  
        nome_jogo = ''  # Variáveis para armazenar dados

        for linha in linhas_dados:  
            try:  
                if float(linha[6]) > preco:  # Transforma em float para comparar com a variavel preco
                    preco = float(linha[6])  
                    nome_jogo = linha[1]  
            except ValueError:  
                continue  
        
        print(f'O jogo mais caro do arquivo é {nome_jogo} e custa {preco} dólares!!!')  

#####################################################
# Execucao do menu e seleçao do arquivo
#####################################################
print('Boas vindas!')
print('Trabalho de: Felipe Pinheiro Fossá') 
print('PUCRS - Banco de dados: ênfase em data analytics')
print('---------------------------------------')
print('')
print('Siga as instruções para fazer os testes.')
print('')

arquivo_csv = input('Digite o nome do arquivo CSV: ') # Escolher arquivo
if arquivo_csv == 'sair':
  print("Programa finalizado")
  raise SystemExit # Finalizaçao do programa antes da abertura de arquivo

carregador = Carregador_de_dados(arquivo_csv)  
linhas_dados = carregador.carregar_dados()  

## Loop do menu

while True:
    print('')
    print('---------------- Menu -----------------')  
    print('1. Visualizar linhas desejadas')  
    print('2. Percentual de jogos pagos e gratuitos')  # Opções do menu
    print('3. Ano mais frequente de lançamentos')  
    print('4. Jogo mais caro do arquivo')
    print('---------------------------------------')
    print('')
    selecionar_opcao = input("Selecione o número (ou digite 'sair' para encerrar): ").lower()  # Deixar tudo em minusculo, 
                                                                                               # facilitar leitura de comandos para finalizar programa
    if selecionar_opcao == 'sair':  
        print("Programa finalizado")  # Finalizar loop e programa
        break  
    elif not selecionar_opcao.isdigit():  
        print("Entrada inválida")  
        continue  # Erro de entrada, loop continua

    selecionar_opcao = int(selecionar_opcao)  # Formatar opcoes para utilizar a class menu
    menu = Menu(selecionar_opcao)  
    menu.opcoes(linhas_dados)
