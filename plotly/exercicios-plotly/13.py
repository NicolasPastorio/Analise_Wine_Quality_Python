## 13. px.choropleth() Mapa Coroplético com Plotly Express
#**Descrição**: O Censo 2022 revelou que a taxa de alfabetização no Brasil é de 93%.
#  No entanto, há variações significativas entre os estados. Por exemplo, Santa Catarina e o Distrito Federal apresentam taxas acima de 97%, enquanto Alagoas e Piauí têm as menores taxas, com 82,3% e 82,8%, respectivamente.

# Instruções:

# Crie um DataFrame com os dados de taxa de alfabetização por estado.

# Utilize um arquivo GeoJSON que contenha os limites geográficos dos estados brasileiros.

# Crie um mapa coroplético com plotly.express.choropleth(), onde:

# As cores representem a taxa de alfabetização.

# O mapa esteja centrado no Brasil.

# Inclua uma barra de cores (colorbar) para indicar os valores.

# Dica:
# Você pode obter um arquivo GeoJSON dos estados brasileiros em fontes como o IBGE ou repositórios públicos no GitHub.

#💡 Desafios Adicionais:
# Adicione interatividade: Mostre o nome do estado e a taxa de alfabetização ao passar o mouse sobre cada região.

# Compare com outros indicadores: Se disponível, adicione dados de outros indicadores, como PIB per capita, para analisar possíveis correlações.

import pandas as pd
# import requests
import plotly.express as px

# Dados fictícios para exemplificação
dados = {
    'estado': ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
               'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
               'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'],
    'taxa_alfabetizacao': [89.1, 82.3, 90.0, 91.5, 85.0, 89.0, 97.0, 96.0, 95.0, 85.5,
                           94.0, 94.5, 95.5, 89.5, 91.0, 96.0, 92.0, 82.8, 96.5, 93.0,
                           97.0, 92.5, 93.5, 97.5, 98.0, 93.0, 94.0],
    'pib_per_capita': [20000, 15000, 21000, 22000, 18000, 19000, 50000, 40000, 35000, 17000,
                       30000, 32000, 33000, 23000, 25000, 45000, 27000, 16000, 47000, 26000,
                       42000, 28000, 22000, 46000, 55000, 24000, 25000]
}

df = pd.DataFrame(dados)

# Carregando o GeoJSON (substitua pelo caminho do seu arquivo)
geojson_file = 'brasil_estados.geojson'

# Criando o mapa Coroplético
fig = px.choropleth(
    df,
    geojson=geojson_file,
    locations='estado',
    featureidkey='properties.sigla',  # Ajuste conforme a estrutura do seu GeoJSON
    color='taxa_alfabetizacao',
    color_continuous_scale='Viridis',
    scope='south america',
    labels={'taxa_alfabetizacao': 'Taxa de Alfabetização (%)'},
    title='Taxa de Alfabetização por Estado (2022)',
    hover_name='estado',
    hover_data={'taxa_alfabetizacao': True, 'pib_per_capita': True}
)

# Ajustando o layout para centralizar o Brasil
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    margin={"r":0,"t":40,"l":0,"b":0},
    coloraxis_colorbar=dict(title="Taxa (%)")
)

# Exibindo o gráfico
# fig.show()
# Gerando arquivo .html do Gráfico
fig.write_html('../graficos-plotly/choropleth-alfabetizacao_por_estado.html')
