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

# 4. Boxplot de qualidade por tipo de vinho
plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='alcohol', data=df)
plt.title('Boxplot de Qualidade por Tipo de Vinho')
plt.xlabel('Qualidade')
plt.ylabel('Álcool')
plt.grid()
plt.savefig('../graficos/white/boxplot_quality.png')  # Salvar o gráfico como um arquivo de imagem
plt.close()  # Fechar a figura
# # O boxplot mostra a distribuição do teor alcoólico em relação à qualidade do vinho.
# # Podemos observar que a maioria dos vinhos de qualidade 5 e 6 tem um teor alcoólico entre 9 e 11%, enquanto os vinhos de qualidade 7 e 8 tendem a ter um teor alcoólico mais elevado, acima de 11%.
# # Além disso, há alguns outliers em todas as qualidades, indicando que existem vinhos com teor alcoólico muito baixo ou muito alto em relação à média.
# # O boxplot é útil para identificar a presença de outliers e a distribuição dos dados em relação à mediana e aos quartis.
# # Compara a qualidade entre vinhos tintos e brancos pode revelar diferenças significativas nas avaliações.