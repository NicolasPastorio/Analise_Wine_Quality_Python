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

# 5. Distribuição do pH
plt.figure(figsize=(10, 6))
sns.histplot(df['ph'], bins=20, kde=True)
plt.title('Distribuição do pH dos Vinhos')
plt.xlabel('pH')
plt.ylabel('Frequência')
plt.grid()
plt.savefig('../graficos/red/hist_ph.png')  # Salvar o gráfico como um arquivo de imagem
plt.close()  # Fechar a figura
# # A distribuição do pH dos vinhos mostra que a maioria dos vinhos tem um pH entre 3 e 4, com uma leve assimetria à direita.
# # O pH é uma medida importante na produção de vinhos, pois influencia o sabor, a cor e a estabilidade do vinho.
# # A distribuição do pH dos vinhos pode ser útil para identificar possíveis problemas na produção ou armazenamento dos vinhos.
# # A análise do pH pode ajudar a entender como ele afeta a qualidade do vinho e a percepção dos consumidores.
# # A distribuição do pH dos vinhos pode indicar aciedez típica dos vinhos no conjunto de dados.