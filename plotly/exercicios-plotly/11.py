## 11. px.sunburst() – Gráfico Sunburst

#**Descrição:** Utilizando o mesmo filtro do exercício anterior,
# construa um gráfico sunburst mostrando a hierarquia: continente → país, com o tamanho representando a população.

import plotly.express as px

# Carregando e filtrando os dados para o ano de 2007
df_gap = px.data.gapminder().query('year == 2007')

# Criando o gráfico sunburst
fig = px.sunburst(df_gap, path=['continent', 'country'],
    values='pop', title="Hierarquia da População por Continente e País (1007)")

#exibir o Gráfico
# fig.show()
# Gerar arquivo .html do gráfico
fig.write_html('../graficos-plotly/sunburst-hierarquia_continente_pais.html')
