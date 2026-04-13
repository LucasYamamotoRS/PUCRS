# Analisador de Dados Meteorológicos - Porto Alegre

Este projeto é uma ferramenta em Python desenvolvida para processar e analisar dados climáticos históricos do município de Porto Alegre, compreendendo o período entre **1961 e 2016**.

O programa permite ao usuário filtrar informações sobre precipitação, temperaturas, umidade e vento, além de gerar visualizações gráficas das médias térmicas.

## Funcionalidades

- **Filtro Personalizado:** Consulta de dados meteorológicos por intervalos de mês e ano.
- **Categorização de Dados:** Opção para visualizar:
  - Todos os dados disponíveis.
  - Apenas dados de precipitação.
  - Dados de temperatura (mínima, máxima e média).
  - Umidade relativa e velocidade do vento.
- **Análise de Precipitação:** Identifica automaticamente o mês/ano mais chuvoso do registro.
- **Estatística de Temperaturas Mínimas:** Calcula a média das temperaturas mínimas para um mês específico entre os anos de 2006 e 2016.
- **Visualização Gráfica:** Gera um gráfico de barras comparativo das temperaturas mínimas anuais utilizando a biblioteca `matplotlib`.

## Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/) (para geração de gráficos)
- Biblioteca padrão `csv` (leitura de arquivos)

## Pré-requisitos

Antes de executar o projeto, você precisará ter o Python instalado e a biblioteca `matplotlib`. 