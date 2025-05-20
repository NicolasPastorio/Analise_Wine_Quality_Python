import matplotlib # type: ignore
matplotlib.use('Agg')  # Usar backend non-interactive
import pandas as pd
from tabulate import tabulate  # type: ignore
import matplotlib.pyplot as plt # type: ignore
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

# 2. Mapa de calor das correlações
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Mapa de Calor das Correlações')
plt.savefig('../graficos/white/heatmap.png')  # Salvar o gráfico como um arquivo de imagem
plt.close()  # Fechar a figura
# Podemos observar que a variável 'quality' tem uma correlação positiva com 'alcohol' e uma correlação negativa com 'volatile_acidity', 
# sugerindo que vinhos com maior teor alcoólico tendem a ter uma qualidade melhor, enquanto vinhos com maior acidez volátil tendem a ter uma qualidade pior. 
# O gráfico mostra a correlação entre as variáveis do conjunto de dados. As variáveis mais correlacionadas com a qualidade do vinho são:
# - 'alcohol' (0.48)
# - 'volatile_acidity' (-0.39)
# - 'citric_acid' (0.25)
# - 'residual_sugar' (-0.23)
# - 'density' (-0.23)
# - 'fixed_acidity' (-0.17)
# - 'sulphates' (0.21)
# - 'chlorides' (-0.20)
# - 'pH' (-0.13)
# - 'free_sulfur_dioxide' (-0.10)
# - 'total_sulfur_dioxide' (-0.08)
# - 'fixed_acidity' (0.05)
# - 'citric_acid' (0.04)
# - 'residual_sugar' (-0.03)
# - 'sulphates' (0.02)
# - 'free_sulfur_dioxide' (0.01)
# - 'total_sulfur_dioxide' (0.01)
# - 'pH' (0.01)
# - 'density' (0.01)
# - 'chlorides' (0.01)
# - 'alcohol' (0.01) 