import pandas as pd

df = pd.reac_csv('https://raw.githubusercontent.com/andrebrum/analise_vinhos/main/winequality-red.csv', sep=';')
df.head()
df.info()
df.describe()
df['quality'].value_counts()
df['quality'].value_counts(normalize=True)
df['quality'].value_counts(normalize=True).plot(kind='bar')
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 5))
sns.countplot(x='quality', data=df)
plt.title('Distribuição da qualidade dos vinhos')
plt.xlabel('Qualidade')
plt.ylabel('Frequência')
plt.show()
df.corr()
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre as variáveis')
plt.show()   