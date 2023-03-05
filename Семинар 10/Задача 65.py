'''Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# file = 'penguins.csv'

# df = pd.read_csv(file)

penguins = sns.load_dataset("penguins")
# print(penguins.head())
# print(penguins.describe())
# print(penguins.columns)
# print(df.head())
# print(df.columns)
# print(df.describe())

# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
# g = sns.PairGrid(penguins[cols])
# print(g.map(sns.scatterplot))
# plt.show()

# sns.scatterplot(data=penguins, x='species', y='island')
# plt.show() # отоброзить график

# sns.scatterplot(data=penguins, x='bill_length_mm', y='species')
# plt.show() # отоброзить график

# sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='bill_length_mm', size='bill_length_mm', sizes=(2, 100))
# plt.show() # отоброзить график

# sns.PairGrid(penguins, hue='species').map(sns.scatterplot).add_legend()
# plt.show() # отоброзить график

# sns.heatmap(data=penguins.corr(numeric_only=True), annot = True)
# plt.show() # отоброзить график

# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# sns.heatmap(data=penguins[cols], annot = True)
# plt.show() # отоброзить график

sns.heatmap(data=penguins.corr(numeric_only=True), annot = True, vmin=-1, vmax=1, center= 0)
plt.show() # отоброзить график