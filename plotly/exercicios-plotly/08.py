## 8. px.area() – Área Preenchida

#**Descrição:** Utilizando a série temporal de temperatura criada, 
# construa um gráfico de área preenchendo a área sob a curva.

import pandas as pd
import plotly.express as px
import numpy as np

# Criando uma série temporal fictícia com dados de temperatura
dates = pd.date_range(start='2025-01-01', periods=30)
temp = np.random.uniform(low=15, high=30, size=30)
df_temp = pd.DataFrame({'Date': dates, 'Temperature': temp})

# Criando o gráfico de área preenchida  
fig = px.area(df_temp, x='Date', y='Temperature',
              title='Variação da Temperatura ao Longo do Tempo',
              labels={'Date': 'Data', 'Temperature': 'Temperatura (°C)'})
# Exibindo o gráfico
# fig.show()
# Salvar o gráfico como HTML
fig.write_html('../graficos-plotly/variacao_temperatura_area.html')