"""

Progrma: Análise de dados meteorológicos.

Descrição: Programa que lê, valida e analisa dados meteorológicos informados pelo usuário.
O programa solicita que o usuário insira a temperatura máxima de cada mês, garantindo que os valores estejam entre -60°C e +50°C.

Após a coleta dos dados, o programa calcula e exibe os seguintes resultados:

- A média anual das temperaturas máximas.
- O total de meses escaldantes (meses com temperaturas acima de 33°C).
- O mês mais escaldante (quente) do ano.
- O mês menos quente do ano.

"""

# intervalo de temperaturas devera ser informado em Celcius, entre -60 graus a +50 graus.
mesesindice = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Marco', 4: 'Abril', 5: 'Maio', 6: 'Junho',
    7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

tempmaxima = 0
mediaanual = 0
mesescaldante = 0
qtdmesesescaldantes = 0
mesmenosquente = 0
mesquente = ''
mesfrio = ''
cont = 1

# Laço que percorre os meses do dicionário utilizando a variável cont.
while cont <= 12:
    tempmaxima = float(input(f'Digite a temperatura referente ao mes de {mesesindice[cont]}: '))
    if tempmaxima < 51 and tempmaxima > -61:
        mediaanual += tempmaxima

        # Verifica e contabiliza (caso verdadeiro) se a temperatura é superior ao parâmetro (> 33°C).
        if tempmaxima > 33:
            qtdmesesescaldantes += 1

        # Se for a primeira iteração (cont == 1), os dados serão armazenados em suas respectivas variáveis.
        if cont == 1:
            mesescaldante = tempmaxima
            mesquente = mesesindice[cont]
            mesmenosquente = tempmaxima
            mesfrio = mesesindice[cont]

        # Armazena o mês mais quente e compara com o atual. Caso a atual seja maior (mais quente), substitui e armazena os novos dados.
        elif tempmaxima > mesescaldante:
            mesescaldante = tempmaxima
            mesquente = mesesindice[cont]

        # Armazena o mês menos quente e compara com o atual. Caso o atual seja menor (menos quente), substitui e armazena os novos dados.
        elif tempmaxima < mesmenosquente:
            mesmenosquente = tempmaxima
            mesfrio = mesesindice[cont]

        cont += 1

    else:
        # Mensagem informando ao usuário que os dados inseridos estão fora dos parâmetros.
        print('Temperatura invalida, informe um valor entre -60°C e 50°C.')


#Exibição dos resultados
print(f'A media anual das temperaturas maximas: {mediaanual/12:.1f}°C')
print(f'Total de meses escaldantes (temperaturas > 33°C): {qtdmesesescaldantes}')
print(f'O mes mais escaldante do ano foi: {mesquente}')
print(f'O mes menos quente do ano foi: {mesfrio}')