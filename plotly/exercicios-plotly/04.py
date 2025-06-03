## 4. px.pie() – Gráfico de Pizza

# **Descrição:** Com base no dataset tips, crie um gráfico de pizza 
# mostrando a proporção de fumantes entre os clientes.

#import numpy as np
import plotly.express as px

# Carregando o dataset tips do Plotly Express
df_tips = px.data.tips()
# Agrupando os dados para contar o número de fumantes e não fumantes
smoking_counts = df_tips['smoker'].value_counts().reset_index()
smoking_counts.columns = ['smoker', 'count']
# Criando o gráfico de pizza
fig = px.pie(smoking_counts, 
             names='smoker', 
             values='count', 
             title='Proporção de Fumantes entre os Clientes',
             color='smoker',
             labels={'smoker': 'Fumante', 'count': 'Contagem'})
# Atualizando o layout do gráfico
fig.update_layout(title_x=0.5, 
                  legend_title_text='Fumante',
                  legend=dict(x=0.8, y=0.5))
# Exibindo o gráfico
# fig.show()
# Salvando o gráfico como HTML
fig.write_html('../graficos-plotly/proporcao_fumantes.html')
# O gráfico de pizza mostra a proporção de fumantes e não fumantes entre os clientes do dataset tips.
