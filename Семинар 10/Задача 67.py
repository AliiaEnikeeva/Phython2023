'''1. Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
# print(penguins.head())

# Замена пустых значений на средние
# penguins.fillna(penguins.mean())

penguins.loc[penguins.bill_length_mm >= 42, 'bill_group'] = 'High'
penguins.loc[(penguins.bill_length_mm > 35) & (penguins.bill_length_mm < 42), 'bill_group'] = 'Middle'
penguins.loc[penguins.bill_length_mm <= 35, 'bill_group'] = 'Low'
print(penguins.head(n=10))

penguins[['bill_length_mm','bill_group']]
penguins.groupby('bill_group')['bill_length_mm'].mean()
penguins.groupby('bill_group')['bill_length_mm'].mean().plot(kind='bar')
plt.show()