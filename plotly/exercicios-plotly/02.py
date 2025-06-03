## 2. px.scatter() – Gráfico de Dispersão

#**Descrição:** Usando o dataset iris, crie um gráfico de dispersão
#  que relacione sepal_width e sepal_length, colorindo os pontos 
# conforme a espécie da flor.

#import numpy as np
import plotly.express as px

# Carregando o dataset iris
df_iris = px.data.iris()

# Criando o gráfico de dispersão
fig = px.scatter(df_iris, x='sepal_width', y='sepal_length', 
        color='species', title='Gráfico de Dispersão: Sepal Width vs Sepal Length')

# Atualizando os rótulos dos eixos
fig.update_layout(
    xaxis_title='Largura da Sépala (cm)', 
    yaxis_title='Comprimento da Sépala (cm)')

# Exibindo o gráfico
# fig.show()
# Salvando o gráfico como HTML
fig.write_html('../graficos-plotly/disp_iris.html')




# Salvando o gráfico como PNG
# fig.write_image('disp_iris.png')
# Salvando o gráfico como JSON
# fig.write_json('disp_iris.json')
# Salvando o gráfico como SVG
# fig.write_image('disp_iris.svg')
# Salvando o gráfico como PDF
# fig.write_image('disp_iris.pdf')
# Salvando o gráfico como JPEG
# fig.write_image('disp_iris.jpeg')
# Salvar o gráfico como WebP
# fig.write_image('disp_iris.webp')