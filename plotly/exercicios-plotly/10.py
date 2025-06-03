## 10. px.treemap() – Treemap

#**Descrição:** Com base no dataset gapminder, filtre os dados
# para o ano de 2007 e crie um treemap que mostre a população dos países, organizados por continente.

#Dica: `df_gap = px.data.gapminder().query('year == 2007')`

import plotly.express as px

# Carregando o dataset gapminder e filtrando para o ano de 2007
df_gap = px.data.gapminder().query('year == 2007')

# Criando o treemap
fig = px.treemap(df_gap, 
                 path=['continent', 'country'], 
                 values='pop',
                 title='População dos Países por Continente (2007)',
                 labels={'pop': 'População', 'continent': 'Continente', 'country': 'País'})
# Atualizando o layout do gráfico
#fig.update_layout(title_x=0.5)
# Exibindo o gráfico
# fig.show()
# Salvando o gráfico como HTML
fig.write_html('../graficos-plotly/populacao_paises_treemap.html')