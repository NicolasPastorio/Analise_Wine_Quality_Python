## 12. px.icicle() – Icicle Chart

#**Descrição:** Ainda com o dataset gapminder filtrado para 2007,
# crie um gráfico icicle mostrando a hierarquia: continente → país, com o tamanho proporcional à expectativa de vida.

import plotly.express as px

# Carregando e filtrando os dados para o ano de 2007
df_gap = px.data.gapminder().query('year == 2007')

# Criando o gráfico Icicle
fig = px.icicle(df_gap, path=['continent', 'country'],
    values='lifeExp', title='Hierarquia de Expectativa de Vida por Continente e País (2007)')

# Exibindo o Gráfico
# fig.show()
# Gerando arquivo html do Gráfico
fig.write_html('../graficos-plotly/icicle-expectativa_de_vida.html')
