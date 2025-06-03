## 3. px.bar() – Gráfico de Barras

#**Descrição:** Utilizando o dataset tips, crie um gráfico 
# de barras que mostre o total de gorjetas médias por dia da semana.

#import numpy as np
import plotly.express as px

df_tips = px.data.tips()
avg_tips = df_tips.groupby('day')['tip'].mean().reset_index()

# Criando o gráfico de barras
fig = px.bar(avg_tips, x='day', y='tip', 
             title='Gorjetas Médias por Dia da Semana',
             labels={'day': 'Dia da Semana', 'tip': 'Gorjeta Média'},
             color='day')
fig.update_layout(xaxis_title='Dia da Semana', yaxis_title='Gorjeta Média')

# Exibindo o gráfico
#fig.show() 
# Salvar o gráfico como HTML
fig.write_html('../graficos-plotly/gorjetas_por_dia.html')
# O gráfico de barras mostra as gorjetas médias por dia da semana,