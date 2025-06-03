## 1. px.histogram() – Histograma

##**Descrição:** Gere uma lista de 1000 valores aleatórios com distribuição normal 
# (média = 0, desvio padrão = 1). Em seguida, construa um histograma para visualizar 
# a distribuição dos dados.

import numpy as np
import plotly.express as px

# Gerando 1000 valores aleatórios com distribuição normal
data = np.random.normal(loc=0, scale=1, size=1000)

# Criando o histograma
fig = px.histogram(data, nbins=30, title='Histograma de Valores Aleatórios com Distribuição Normal')
fig.update_layout(xaxis_title='Valor', yaxis_title='Frequência')
# Exibindo o gráfico
#fig.show()
# Salvar o gráfico como HTML
fig.write_html('../graficos-plotly/histograma.html')





# Salvar o gráfico como PNG
#fig.write_image('histograma.png')
# Salvar o gráfico como JSON
#fig.write_json('histograma.json')
# Salvar o gráfico como SVG
#fig.write_image('histograma.svg')
# Salvar o gráfico como PDF
#fig.write_image('histograma.pdf')
# Salvar o gráfico como JPEG
#fig.write_image('histograma.jpeg')
