import csv
from time import sleep
import matplotlib.pyplot as plt





def carregararq(nome_arquivo):
    """Lê o CSV e retorna os dados ignorando o cabeçalho."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)  # Pula o cabeçalho de forma limpa
            return list(leitor)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return []


def chuvoso (arquivo):
    """
        Calcula o acumulado de precipitação por mês/ano e identifica o período mais chuvoso.
        Retorna um dicionário mapeando 'mês/ano' ao total de precipitação acumulada."""

    maischuvoso = {}
    for item in arquivo:
        mesano = item[0][3:]
        if mesano not in maischuvoso:
            maischuvoso[mesano] = 0
        maischuvoso[mesano] += float(item[1])
    ordenado = sorted(maischuvoso.items(), key=lambda x: x[1], reverse=True)
    print(f'A maior precipitacao foi de: \033[34m{ordenado[0][1]}\033[m')
    print(f'O mes/ano mais chuvoso registrado durante este periodo foi: \033[34m{ordenado[0][0]}\033[m')
    lin()
    return maischuvoso


def mtemp (arquivo, tempmin):
    """
        Calcula a média das temperaturas mínimas para um mês específico entre 2006 e 2016.
        Retorna um dicionário com a média de temperatura mínima para cada ano do intervalo.
        """

    indicemin = {}
    qtdias = {}

    for c in range(2006, 2017):
        datamin = tempmin + '/' + str(c)
        for item in arquivo:
            if datamin not in indicemin:
                indicemin[datamin] = 0
                qtdias[datamin] = 0
            if item[0][3:] == datamin:
                indicemin[datamin] += float(item[3])
                qtdias[datamin] += 1
        if qtdias[datamin] > 0:
            print(f'{datamin} -> \033[34m{indicemin[datamin] / qtdias[datamin]:.2f}℃\033[m')
            indicemin[datamin] = indicemin[datamin] / qtdias[datamin]
    lin()
    return indicemin

#Gerar grafico.
def grafico(lst):
    """
        Gera e exibe um gráfico de barras das médias de temperaturas mínimas.
    """

    temp = lst.keys()
    data = lst.values()

    plt.title('Media de temperaturas minimas')
    plt.xlabel('Data (mes/ano)')
    plt.ylabel('Temperatura ℃')

    plt.bar(temp, data, width=0.4, color='blue', label='Temp Min')
    plt.legend(loc='best')

    plt.show()

#Funcao printar meses.
def im():
    """
    Exibe no console a legenda de meses e seus respectivos códigos numéricos.
    """
    print('Janeiro - 01, Fevereiro - 02, Marco - 03, Abril - 04, Maio - 05, Junho - 06,\n'
          'Julho - 07, Agosto - 08, Setembro - 09, Outubro - 10, Novembro - 11, Dezembro - 12')


def lin():
    """Imprime uma linha divisória estilizada no console para melhor legibilidade."""
    print('\033[34m-=\033[m' * 50)




arquivo = carregararq('Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv')

cabecalho = ["Data", "Precipitacao", "Temperatura maxima", "Temperatura minima", "Horas de insolacao",
                 "Temperatura media", "Umidade relativa", " Velocidade vento"]

indicemeses = {
    '01': 'Janeirio', '02': 'Fevereiro', '03': 'Marco', '04': 'Abril',
    '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
    '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
}


print('Este programa demonstra os dadas meteorologicos do municipio brasileiro de Porto Alegre,'
      'entre os anos 1961 e 2016.\n'
      'Informe o intervalo de tempo (mes/ano), que gostaria de visualizar os dados.')
lin()
sleep(2)
im()

# Validação do mês inicial
while True:
    lin()
    print('\033[33mObs: Necessario utilizar duas casas decimais. Ex: 01, 02...\033[m')
    mesinicial = str(input('Digite o mes inicial que gostaria de visualizar os dados (01~12)): ')).strip()
    if mesinicial in indicemeses:
        break
    else:
        print('\033[031mERRO. Digite um valor no intervalo valido.\033[m')
        lin()
        im()


# Validação do ano inicial
while True:
    lin()
    print('Digite o ano inicial entre 1961 e 2016 para visualizar os dados.')
    anoinicial = int(input('Digite o ano inicial que gostaria de visualizar os dados: '))
    if 1961 <= anoinicial <= 2016:
        break
    else:
        print('\033[031mERRO. Digite um valor no intervalo valido.\033[m')

# Validação do mês final
im()
while True:
    lin()
    print('\033[33mObs: Necessario utilizar duas casas decimais. Ex: 01, 02...\033[m')
    mesfinal = str(input('Digite o mes final que gostaria de visualizar os dados (01~12): ')).strip()
    if mesfinal in indicemeses:
        break
    else:
        print('\033[031mERRO. Digite um valor no intervalo valido.\033[m')
        lin()
        im()

# Validação do ano final (garante ordem cronológica)
while True:
    lin()
    print('Digite o ano final entre 1961 e 2016 para visualizar os dados.')
    anofinal = int(input('Digite o ano final que gostaria de visualizar os dados: '))
    if 1961 <= anofinal <= 2016 and anoinicial <= anofinal:
        break
    else:
        print('\033[031mERRO. Digite um valor no intervalo valido.\033[m')
        print('\033[031mERRO. O ano final deve ser superior ao inicial.\033[m')

datainicial = mesinicial + '/' + str(anoinicial)
datafinal = mesfinal + '/' + str(anofinal)

# Escolha do tipo de visualização
while True:
    lin()
    print('Digite quais dados gostaria de visualizar.')
    print('[1] Todos os dados\n'
          '[2] Dados de precipitacao\n'
          '[3] Dados de temperatura\n'
          '[4] Dados de umidade e vento')
    opcao = int(input())
    if opcao >= 1 and opcao < 5:
        break
    else:
        print('\033[031mERRO. Digite um valor no intervalo valido.\033[m')


# Filtragem e exibição conforme opção escolhida
if opcao == 1:
    print(cabecalho)
    for item in arquivo:
        if item[0][3:] == datainicial:
            print(item)
        if item[0][3:] == datafinal:
            print(item)
if opcao == 2:
    print(cabecalho[1])
    for item in arquivo:
        if item[0][3:] == datainicial:
            print(item[1])
        if item[0][3:] == datafinal:
            print(item[1])
if opcao == 3:
    print(cabecalho[2:6])
    for item in arquivo:
        if item[0][3:] == datainicial:
            print(item[2:6])
        if item[0][3:] == datafinal:
            print(item[2:6])
if opcao == 4:
    print(cabecalho[6:])
    for item in arquivo:
        if item[0][3:] == datainicial:
            print(item[6:])
        if item[0][3:] == datafinal:
            print(item[6:])
lin()
sleep(2)

# Análise de precipitação
chuvoso(arquivo)

im()

# Análise de médias mínimas (2006-2016)
while True:
    lin()
    print('\033[33mObs: Necessario utilizar duas casas decimais. Ex: 01, 02...\033[m')
    tempmin = str(input('Digite o mes que gostaria de visualizar os dados (01~12): ')).strip()
    if tempmin in indicemeses:
        break
    else:
        print('\033[031mERRO. Digite um valor no intervalo valido.\033[m')
        lin()
        im()


lista = mtemp(arquivo, tempmin)

# Limpeza de dados nulos antes do cálculo da média e gráfico
for k, v in list(lista.items()):
    if v == 0:
        del lista[k]

# Média de temperatura
media = sum(lista.values())/len(lista)

# Gráfico das temperaturas mínimas
grafico(lista)



# Calcula e exibe a média de temperatura
print(f'A media geral da temperatura do mes de \033[32m{indicemeses.get(tempmin)}\033[m, '
      f'dentro do periodo de \033[32m2006~2016\033[m foi de: \033[34m{media:.2f}\033[m')


































