import csv  

######################################################  
## Carregar dados csv:  
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

        except FileNotFoundError:  
            print("Erro ao carregar dados, nome ou arquivo não identificado.")  
            print("Programa finalizado, tente novamente.")  
            raise SystemExit  

#####################################################  
# Entrada do menu  
#####################################################  

class Menu:  
    def __init__(self, selecionar_opcao):  
        self.selecionar_opcao = selecionar_opcao  

    def opcoes(self, linhas_dados):  
        match self.selecionar_opcao:  
            case 1:  
                self.visualizar_linhas(linhas_dados)  
            case 2:  
                self.percentual_jogos(linhas_dados)  
            case 3:  
                self.data_mais_lancamentos(linhas_dados)  
            case 4:  
                self.jogo_mais_caro(linhas_dados)  
            case _:  
                print('Opção não válida, selecione um numero descrito no menu.')  

    def visualizar_linhas(self, linhas_dados):  
        count = int(input('Quantas linhas deseja visualizar: '))  
        for freio, line in enumerate(linhas_dados, start=1):  
            print(line)  # A linha já é uma lista  
            if freio == count:  
                break  

    def percentual_jogos(self, linhas_dados):  
        gratuito = 0  
        pago = 0  
        total_linhas = 0  

        for line in linhas_dados:  
            preco = line[6]  
            total_linhas += 1  
            
            if preco == '0.0':  
                gratuito += 1  
            else:  
                pago += 1  # Corrigido para "pago += 1"  

        if total_linhas > 0:  # Evita divisão por zero  
            porcentagem_jogosgratuitos = (gratuito / total_linhas) * 100  
            porcentagem_jogospagos = (pago / total_linhas) * 100  

            print(f"% de jogos gratuitos: {porcentagem_jogosgratuitos:.2f}")  
            print(f"% de jogos pagos: {porcentagem_jogospagos:.2f}")  

    def data_mais_lancamentos(self, linhas_dados):  
        contagem_datas = {}  

        for linha in linhas_dados:  
            data_lancamento = linha[2]  
            if data_lancamento in contagem_datas:  
                contagem_datas[data_lancamento] += 1  
            else:  
                contagem_datas[data_lancamento] = 1  

        if contagem_datas:  # Verifica se há dados  
            ano_mais_frequente = max(contagem_datas, key=contagem_datas.get)  
            print(f'O ano mais frequente de lançamentos é: {ano_mais_frequente[6:]}')  

    def jogo_mais_caro(self, linhas_dados):  
        preco = 0  
        nome_jogo = ''  

        for linha in linhas_dados:  
            try:  
                if float(linha[6]) > preco:  
                    preco = float(linha[6])  
                    nome_jogo = linha[1]  
            except ValueError:  
                continue  
        
        print(f'O jogo mais caro do arquivo é {nome_jogo} e custa {preco} dólares!!!')  


# Executando o programa  
arquivo_csv = input('Digite o nome do arquivo CSV: ')
carregador = Carregador_de_dados(arquivo_csv)  
linhas_dados = carregador.carregar_dados()  

while True:
    print('')
    print('---------------- Menu -----------------')  
    print('1. Visualizar linhas desejadas')  
    print('2. Percentual de jogos pagos e gratuitos')  
    print('3. Ano mais frequente de lançamentos')  
    print('4. Jogo mais caro do arquivo')
    print('---------------------------------------')
    print('')
    selecionar_opcao = input("Selecione o número (ou digite 'sair' para encerrar): ").lower()  

    if selecionar_opcao == 'sair':  
        print("Programa finalizado")  
        break  
    elif not selecionar_opcao.isdigit():  
        print("Entrada inválida")  
        continue  

    selecionar_opcao = int(selecionar_opcao)  
    menu = Menu(selecionar_opcao)  
    menu.opcoes(linhas_dados)
