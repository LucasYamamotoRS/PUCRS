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

#Dicionário/Indice que associa o número ao nome do respectivo mês.
mesesindice = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Marco', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

#Variaveis utilizadas:
mediamaximaanual = 0
qtdmesesescaldantes = 0
mesmaisescaldante = -61
mesmenosquente = 51
mesquente = ''
mesfrio = ''

#Primeiro laço: Refere-se aos 12 meses do ano, dos quais serão coletadas as temperaturas máximas de cada mês inseridas pelo usuário.
for meses in range (1, 13):
    #Segundo laço: Usado para verificação dos dados inseridos pelo usuário. Caso estejam fora dos parâmetros, o usuário podera reinseri-lo novamente.
    #Caso estejam dentro dos parâmetros, os dados são coletados e o laço é interrompido pelo comando "break".
    for tentativa in range (100):
        tempmaxima = float(input('Digite a temperatura do mes {}: '.format(meses)))
        #Verifica se a temperatura está dentro do intervalo (-60°C e +50°C).
        if tempmaxima < 51 and tempmaxima > -61:
            mediamaximaanual += tempmaxima
            #Verifica e contabiliza (caso verdadeira) se a temperatura é superior ao parâmetro (> 33°C).
            if tempmaxima > 33:
                qtdmesesescaldantes += 1
            #Armazena o mês mais quente e compara com o atual. Caso a atual seja maior (mais quente), substitui e armazena os novos dados.
            if tempmaxima > mesmaisescaldante:
                mesmaisescaldante = tempmaxima
                mesquente = mesesindice.get(meses)
            #Armazena o mês menos quente e compara com o atual. Caso o atual seja menor (menos quente), substitui e armazena os novos dados.
            if tempmaxima < mesmenosquente:
                mesmenosquente = tempmaxima
                mesfrio = mesesindice.get(meses)
            break
        #Mensagem informando ao usuário que os dados inseridos estão fora dos parâmetros.
        else:
            print('Temperatura invalida, informe um valor entre -60°C e 50°C.')

#Exibição dos resultados.
print('A media anual das temperaturas maximas: {:.1f}°C'.format(mediamaximaanual/12))
print('Total de meses escaldantes (temperaturas > 33°C): {}'.format(qtdmesesescaldantes))
print('O mes mais escaldante do ano foi: {}'.format(mesquente))
print('O mes menos quente do ano foi: {}'.format(mesfrio))