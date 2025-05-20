import matplotlib
matplotlib.use('Agg')  # Usar backend non-interactive
import pandas as pd
from tabulate import tabulate  # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns  # type: ignore

# Carregar os dados
df = pd.read_csv('../wine+quality/winequality-white.csv', sep=';')
# df = pd.read_csv('https://raw.githubusercontent.com/andrebrum/analise_vinhos/main/winequality-red.csv', sep=';')

# Verificação e tratamento dos valores ausentes
missing_values = df.isnull().sum()
missing_values_df = pd.DataFrame(missing_values, columns=['Valores ausentes'])
print("Valores ausentes em cada coluna:\n")
print(tabulate(missing_values_df, headers='keys', tablefmt='psql'))

# Verifica tipos de dados
print('Tipos de dados:\n', df.dtypes)

# Renomear colunas para facilitar a leitura
df.columns = [col.replace(' ', '_').lower() for col in df.columns]

# 3. Dispersão entre álcool e qualidade
plt.figure(figsize=(10, 6))
sns.scatterplot(x='alcohol', y='quality', data=df, alpha=0.6)
plt.title('Dispersão entre Álcool e Qualidade do Vinho')
plt.xlabel('Álcool')
plt.ylabel('Qualidade')
plt.grid()
plt.savefig('../graficos/red/scatter_alcohol_quality.png')  # Salvar o gráfico como um arquivo de imagem
plt.close()  # Fechar a figura
# A dispersão entre álcool e qualidade do vinho mostra uma tendência de que vinhos com maior teor alcoólico tendem a ter uma qualidade melhor.
# No entanto, há uma certa dispersão nos dados, indicando que outros fatores também podem influenciar a qualidade do vinho.

