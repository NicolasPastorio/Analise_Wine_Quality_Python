import matplotlib
matplotlib.use('Agg')  # Usar backend non-interactive
import pandas as pd
from tabulate import tabulate  # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns  # type: ignore

# Carregar os dados
df = pd.read_csv('winequality-white.csv', sep=';')
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

# 1. Histograma de variável alvo (quality)
plt.figure(figsize=(8, 6))
sns.histplot(df['quality'], bins=10, kde=True)
plt.title('Distribuição da Qualidade do Vinho')
plt.xlabel('Qualidade')
plt.ylabel('Frequência')
plt.xticks(range(3, 10))
plt.grid(axis='y')
plt.savefig('graficos/hist_quality.png')  # Salvar o gráfico como um arquivo de imagem
plt.close()  # Fechar a figura
# A maioria dos vinhos possui uma qualidade entre 5 e 6, com uma distribuição ligeiramente assimétrica à direita.

# Gráfico de dispersão entre variáveis
plt.figure(figsize=(12, 8))
sns.pairplot(df, hue='quality', diag_kind='kde', markers='o')
plt.suptitle('Gráfico de Dispersão entre Variáveis', y=1.02)
plt.savefig('graficos/pairplot.png')  # Salvar o gráfico como um arquivo de imagem
plt.close()  # Fechar a figura

print("Gráficos salvos com sucesso!")