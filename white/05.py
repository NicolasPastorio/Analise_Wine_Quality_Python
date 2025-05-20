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

# 6. Relação entre acidez e qualidade

plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='fixed_acidity', data=df)
plt.title('Relação entre Acidez Fixa e Qualidade dos Vinhos')
plt.xlabel('Qualidade')
plt.ylabel('Acidez Fixa')
plt.grid()
plt.savefig('../graficos/white/boxplot_acidez_fixa.png')  # Salvar o gráfico como um arquivo de imagem
plt.close()  # Fechar a figura
# # A relação entre acidez fixa e qualidade dos vinhos mostra que a maioria dos vinhos de alta qualidade tem uma acidez fixa mais baixa.
# # A acidez fixa é uma medida importante na produção de vinhos, pois influencia o sabor e a estabilidade do vinho.
# Uma acides volátil mais alta pode estar associada a uma qualidade inferior do vinho.
# # A análise da relação entre acidez e qualidade pode ajudar a entender como esses fatores afetam a percepção dos consumidores.

# Conclusão
# A análise exploratória do conjunto de dados Wine Quality revelou insights valiosos sobre os fatores
# que influenciam a qualidade dos vinhos portugueses. Variáveis como teor alcoólico e acidez volátil 
# mostram correlações significativas com a qualidade, indicando que vinhos com maior teor alcoólico e menor acidez volátil tendem a ser avaliados mais positivamente.
# Além disso, a distribuição do pH dos vinhos sugere uma acidez típica, com a maioria dos vinhos apresentando pH entre 3 e 4.