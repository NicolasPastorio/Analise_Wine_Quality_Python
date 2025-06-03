## 7. px.line() – Gráfico de Linha

# **Descrição:** Crie uma série temporal fictícia com dados de
#  temperatura para os últimos 30 dias. Em seguida, plote um gráfico de linha mostrando a variação da temperatura ao longo do tempo.
import pandas as pd
import plotly.express as px
import numpy as np

# Criando uma série temporal fictícia com dados de temperatura
dates = pd.date_range(start='2025-01-01', periods=30)
temp = np.random.uniform(low=15, high=30, size=30)
df_temp = pd.DataFrame({'Date': dates, 'Temperature': temp})

# Criando o gráfico de linha
fig = px.line(df_temp, x='Date', y='Temperature',
              title='Variação da Temperatura ao Longo do Tempo',
              labels={'Date': 'Data', 'Temperature': 'Temperatura (°C)'})
# Exibindo o gráfico
# fig.show()
# Salvar o gráfico como HTML
fig.write_html('../graficos-plotly/variacao_temperatura.html')