'''Изобразить гистограмму по flipper_length_mm
с оттенком height_group. Сделать анализ'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

penguins.loc[penguins.flipper_length_mm >= 213, 'height_group'] = 'High'
penguins.loc[(penguins.flipper_length_mm > 190) & (penguins.flipper_length_mm < 213), 'height_group'] = 'Middle'
penguins.loc[penguins.flipper_length_mm <= 190, 'height_group'] = 'Low'
print(penguins.head())

sns.histplot(data=penguins, x='flipper_length_mm', hue='height_group')
plt.show()