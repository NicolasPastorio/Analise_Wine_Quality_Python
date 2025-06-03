## 9. px.density_heatmap() – Mapa de Calor de Densidade

#**Descrição:** Usando o dataset iris, construa um mapa de calor 
# de densidade para as variáveis sepal_length e sepal_width.

import plotly.express as px
# Carregando o dataset iris do Plotly Express
df_iris = px.data.iris()

# Criando o mapa de calor de densidade
fig = px.density_heatmap(df_iris, 
                         x='sepal_length', 
                         y='sepal_width', 
                         title='Mapa de Calor de Densidade - Iris Dataset',
                         labels={'sepal_length': 'Comprimento da Sépala (cm)', 
                                 'sepal_width': 'Largura da Sépala (cm)'})
# Atualizando o layout do gráfico
#fig.update_layout(title_x=0.5)
# Exibindo o gráfico
# fig.show()
# Salvando o gráfico como HTML
fig.write_html('../graficos-plotly/mapa_calor_densidade_iris.html')