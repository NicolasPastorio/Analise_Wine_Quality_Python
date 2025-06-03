## 5. px.box() – Boxplot

# **Descrição:** Crie um boxplot para mostrar a distribuição de petal_length por espécie no dataset iris.

import plotly.express as px
# Carregando o dataset iris do Plotly Express
df_iris = px.data.iris()
# Criando o boxplot
fig = px.box(df_iris, 
             x='species', 
             y='petal_length', 
             title='Distribuição de Petal Length por Espécie',
             color='species',
             labels={'species': 'Espécie', 'petal_length': 'Comprimento da Pétala'})
# Atualizando o layout do gráfico
fig.update_layout(title_x=0.5, 
                  legend_title_text='Espécie',
                  legend=dict(x=0.8, y=0.5))
# Exibindo o gráfico
# fig.show()
# Salvando o gráfico como HTML
fig.write_html('../graficos-plotly/distribuicao_petal_length.html')


# O boxplot mostra a distribuição do comprimento das pétalas (petal_length) por espécie no dataset iris.
# Cada caixa representa a distribuição dos dados para cada espécie,
# permitindo visualizar a mediana, os quartis e os valores atípicos (outliers).
# O boxplot é útil para comparar a distribuição de uma variável numérica entre diferentes categorias,
# neste caso, as espécies de flores no dataset iris.
# O boxplot é uma ferramenta poderosa para visualizar a distribuição de dados,
# especialmente quando se deseja comparar múltiplas categorias.
# Ele permite identificar rapidamente a mediana, os quartis e possíveis valores atípicos,
# fornecendo uma visão clara da dispersão dos dados.
# O gráfico gerado pode ser salvo como um arquivo HTML para visualização posterior,