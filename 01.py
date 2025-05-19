import pandas as pd
from tabulate import tabulate
# carregar os dados
df = pd.read_csv('winequality-white.csv', sep=';')
#df = pd.read_csv('https://raw.githubusercontent.com/andrebrum/analise_vinhos/main/winequality-red.csv', sep=';')

# Verificação e tratamento dos valores auzentes
missing_values = df.isnull().sum()
missing_values_df = pd.DataFrame(missing_values, columns=['Valores ausentes'])
print("Valores ausentes em cada coluna:\n")
print(tabulate(missing_values_df, headers='keys', tablefmt='psql'))
# Verifica 