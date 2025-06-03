## 6. px.violin() – Gráfico de Violino

# **Descrição:** Construa um gráfico de violino para analisar a distribuição dos valores
#  de total_bill por sexo no dataset tips. Adicione pontos individuais.

#import numpy as np
import plotly.express as px

df_tips = px.data.tips()

# Criando o gráfico de violino
fig = px.violin(df_tips, x="sex", y='total_bill',
    points="all", title="Distribuição de Total de Contas por Sexo")
fig.update_layout(xaxis_title='Sexo', yaxis_title='Total da Conta')
# Exibindo o gráfico
# fig.show()
# Salvar o gráfico como HTML
fig.write_html('../graficos-plotly/violino_total_bill_por_sexo.html')


